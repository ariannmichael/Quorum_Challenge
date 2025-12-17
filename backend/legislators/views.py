from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.db import connection
import csv

from legislators.models import Legislator
from legislators.serializers import LegislatorVoteAnalyticsSerializer


class LegislatorVoteAnalyticsView(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT legislator.id, legislator.name,
                (SELECT COUNT(*) from vote_results_vote_result as vr WHERE vr.legislator_id = legislator.id AND vr.vote_type = 1) as supported_bills,
                (SELECT COUNT(*) from vote_results_vote_result as vr WHERE vr.legislator_id = legislator.id AND vr.vote_type = 2) as opposed_bills
                FROM legislators_legislator AS legislator
            """)
            rows = cursor.fetchall()

            legislators = [
                {
                    "legislator": {"id": row[0], "name": row[1]},
                    "supported_bills": row[2],
                    "opposed_bills": row[3]
                }
                for row in rows
            ]

        serializer = LegislatorVoteAnalyticsSerializer(legislators, many=True)
        return Response(serializer.data)

    def post(self, request):
        if 'file' not in request.FILES:
            return Response({'message': 'No file provided'}, status=400)

        csv_file = request.FILES['file']
        if isinstance(csv_file, str):
            decoded_file = csv_file.splitlines()
        else:
            decoded_file = csv_file.read().decode('utf-8').splitlines()

        csv_reader = csv.DictReader(decoded_file)

        legislators_data = []
        for row in csv_reader:
            legislators_data.append({'id': row['id'], 'name': row['name']})

        # Bulk insert using Django ORM
        BATCH_SIZE = 1000
        legislators_objects = [
            Legislator(id=int(row['id']), name=row['name'])
            for row in legislators_data
        ]

        # Use bulk_create with ignore_conflicts for ON CONFLICT DO NOTHING behavior
        for i in range(0, len(legislators_objects), BATCH_SIZE):
            batch = legislators_objects[i:i + BATCH_SIZE]
            Legislator.objects.bulk_create(batch, ignore_conflicts=True)

        return Response({'message': 'Legislator CSV file uploaded successfully'}, status=201)


class LegislatorAnalyticsExportCSV(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT legislator.id, legislator.name,
                (SELECT COUNT(*) from vote_results_vote_result as vr WHERE vr.legislator_id = legislator.id AND vr.vote_type = 1) as supported_bills,
                (SELECT COUNT(*) from vote_results_vote_result as vr WHERE vr.legislator_id = legislator.id AND vr.vote_type = 2) as opposed_bills
                FROM legislators_legislator AS legislator
            """)
            rows = cursor.fetchall()

            legislators = [
                {
                    "id": row[0],
                    "name": row[1],
                    "num_supported_bills": row[2] if row[2] is not None else 0,
                    "num_opposed_bills": row[3] if row[3] is not None else 0
                }
                for row in rows
            ]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="legislators-support-oppose-count.csv"'

        writer = csv.writer(response)
        writer.writerow(["id", "name", "num_supported_bills", "num_opposed_bills"])

        for legislator in legislators:
            writer.writerow((
                legislator["id"],
                legislator["name"],
                legislator["num_supported_bills"],
                legislator["num_opposed_bills"]
            ))

        return response

