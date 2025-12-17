from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.db import connection
import csv

from bills.models import Bill
from bills.serializers import BillAnalyticsSerializer


class BillAnalyticsAPIView(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT bill.id, bill.title,
                    COUNT(CASE WHEN vr.vote_type = 1 THEN 1 END) AS supporters,
                    COUNT(CASE WHEN vr.vote_type = 2 THEN 1 END) AS opposers,
                    bill.primary_sponsor
                FROM bills_bill as bill
                LEFT JOIN votes_vote AS v ON v.bill_id = bill.id
                LEFT JOIN vote_results_vote_result AS vr ON vr.vote_id = v.id
                GROUP BY bill.id, bill.title, bill.primary_sponsor;
            """)
            rows = cursor.fetchall()

            bill_analytics = [
                {
                    "bill": {"id": row[0], "title": row[1], "primary_sponsor": row[4]},
                    "supporters": row[2],
                    "opposers": row[3],
                }
                for row in rows
            ]

        serializer = BillAnalyticsSerializer(bill_analytics, many=True)
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

        bill_data = []
        for row in csv_reader:
            bill_data.append({
                'id': int(row['id']),
                'title': row['title'],
                'primary_sponsor': int(row['sponsor_id']) if row.get('sponsor_id') else None
            })

        # Bulk insert using Django ORM
        BATCH_SIZE = 1000
        bill_objects = [
            Bill(id=row['id'], title=row['title'], primary_sponsor=row['primary_sponsor'])
            for row in bill_data
        ]

        # Use bulk_create with ignore_conflicts for ON CONFLICT DO NOTHING behavior
        for i in range(0, len(bill_objects), BATCH_SIZE):
            batch = bill_objects[i:i + BATCH_SIZE]
            Bill.objects.bulk_create(batch, ignore_conflicts=True)

        return Response({'message': 'Bill CSV file uploaded successfully'}, status=201)


class BillAnalyticsExportCSV(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT bill.id, bill.title,
                    COUNT(CASE WHEN vr.vote_type = 1 THEN 1 END) AS supporters,
                    COUNT(CASE WHEN vr.vote_type = 2 THEN 1 END) AS opposers,
                    bill.primary_sponsor
                FROM bills_bill as bill
                LEFT JOIN votes_vote AS v ON v.bill_id = bill.id
                LEFT JOIN vote_results_vote_result AS vr ON vr.vote_id = v.id
                GROUP BY bill.id, bill.title, bill.primary_sponsor;
            """)
            rows = cursor.fetchall()

            bill_analytics = [
                {
                    "bill": {"id": row[0], "title": row[1], "primary_sponsor": row[4]},
                    "supporters": row[2],
                    "opposers": row[3],
                }
                for row in rows
            ]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="bills.csv"'

        writer = csv.writer(response)
        writer.writerow(["id", "title", "supporter_count", "opposer_count", "primary_sponsor"])

        for row in bill_analytics:
            writer.writerow((row["bill"]["id"], row["bill"]["title"], row["supporters"], row["opposers"], row["bill"]["primary_sponsor"]))

        return response

