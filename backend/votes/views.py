from rest_framework.views import APIView
from rest_framework.response import Response
import csv

from votes.models import Vote


class VotesAPIView(APIView):
    def post(self, request):
        if 'file' not in request.FILES:
            return Response({'message': 'No file provided'}, status=400)

        csv_file = request.FILES['file']
        if isinstance(csv_file, str):
            decoded_file = csv_file.splitlines()
        else:
            decoded_file = csv_file.read().decode('utf-8').splitlines()

        csv_reader = csv.DictReader(decoded_file)

        votes_data = []
        for row in csv_reader:
            votes_data.append({'id': row['id'], 'bill_id': row['bill_id']})

        # Bulk insert using Django ORM
        BATCH_SIZE = 1000
        vote_objects = [
            Vote(id=int(row['id']), bill_id=int(row['bill_id']))
            for row in votes_data
        ]

        # Use bulk_create with ignore_conflicts for ON CONFLICT DO NOTHING behavior
        for i in range(0, len(vote_objects), BATCH_SIZE):
            batch = vote_objects[i:i + BATCH_SIZE]
            Vote.objects.bulk_create(batch, ignore_conflicts=True)

        return Response({'message': 'Votes CSV file uploaded successfully'}, status=201)

