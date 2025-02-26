from rest_framework.views import APIView
from rest_framework.response import Response

from bills.infrastructure.db.repositories import BillRepository
from bills.application.use_cases import GetBillStatsUseCase, ImportBillsFromCSVUseCase
from bills.infrastructure.api.serializers import BillStatsSerializer


class BillStatsAPIView(APIView):
    def get(self, request):
        repo = BillRepository()
        use_case = GetBillStatsUseCase(repo)
        bill_stats = use_case.execute()

        serializer = BillStatsSerializer(bill_stats, many=True)
        return Response(serializer.data)


    def post(self, request):
        if 'file' not in request.FILES:
            return Response({'message': 'No file provided'}, status=400)

        repo = BillRepository()
        use_case = ImportBillsFromCSVUseCase(repo)
        result = use_case.execute(request.FILES['file'])


        return Response(result, status=201)
