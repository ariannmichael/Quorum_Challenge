from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
import csv

from bills.infrastructure.db.repositories import BillRepository
from bills.application.use_cases import GetBillAnalyticsUseCase, ImportBillsFromCSVUseCase
from bills.infrastructure.api.serializers import BillAnalyticsSerializer


class BillAnalyticsAPIView(APIView):
    def get(self, request):
        repo = BillRepository()
        use_case = GetBillAnalyticsUseCase(repo)
        bill_analytics = use_case.execute()

        serializer = BillAnalyticsSerializer(bill_analytics, many=True)
        return Response(serializer.data)


    def post(self, request):
        if 'file' not in request.FILES:
            return Response({'message': 'No file provided'}, status=400)

        repo = BillRepository()
        use_case = ImportBillsFromCSVUseCase(repo)
        result = use_case.execute(request.FILES['file'])


        return Response(result, status=201)


class BillAnalyticsExportCSV(APIView):
    def get(self, request):
        repo = BillRepository()
        use_case = GetBillAnalyticsUseCase(repo)
        bill_analytics = use_case.execute()

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="bills.csv"'

        writer = csv.writer(response)
        writer.writerow(["id", "title", "supporter_count", "opposer_count", "primary_sponsor"])

        for row in bill_analytics:
            writer.writerow((row["bill"].id, row["bill"].title, row["supporters"], row["opposers"], row["bill"].primary_sponsor))

        return response