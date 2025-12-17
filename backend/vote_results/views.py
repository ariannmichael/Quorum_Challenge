from rest_framework.views import APIView
from rest_framework.response import Response
import csv

from vote_results.models import VoteResult
from legislators.models import Legislator
from votes.models import Vote


class VoteResultsAPIView(APIView):
    def post(self, request):
        if 'file' not in request.FILES:
            return Response({'message': 'No file provided'}, status=400)

        csv_file = request.FILES['file']
        if isinstance(csv_file, str):
            decoded_file = csv_file.splitlines()
        else:
            decoded_file = csv_file.read().decode('utf-8').splitlines()

        csv_reader = csv.DictReader(decoded_file)

        vote_results_data = []
        for row in csv_reader:
            vote_results_data.append({
                'id': row['id'],
                'legislator_id': row['legislator_id'],
                'vote_id': row['vote_id'],
                'vote_type': row['vote_type']
            })

        # Filter out invalid entries
        valid_vote_results = []
        for row in vote_results_data:
            legislator_id = row['legislator_id']
            vote_id = row['vote_id']

            if not Legislator.objects.filter(id=legislator_id).exists():
                print(f"Legislator {legislator_id} does not exist.")
                continue

            if not Vote.objects.filter(id=vote_id).exists():
                print(f"Vote {vote_id} does not exist.")
                continue

            valid_vote_results.append(row)

        # Bulk insert using Django ORM
        BATCH_SIZE = 1000
        vote_result_objects = [
            VoteResult(
                id=int(row['id']),
                legislator_id=int(row['legislator_id']),
                vote_id=int(row['vote_id']),
                vote_type=int(row['vote_type'])
            )
            for row in valid_vote_results
        ]

        # Use bulk_create with ignore_conflicts for ON CONFLICT DO NOTHING behavior
        for i in range(0, len(vote_result_objects), BATCH_SIZE):
            batch = vote_result_objects[i:i + BATCH_SIZE]
            VoteResult.objects.bulk_create(batch, ignore_conflicts=True)

        return Response({'message': 'Vote Results CSV file uploaded successfully'}, status=201)

