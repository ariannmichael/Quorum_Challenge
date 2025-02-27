from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
import csv

from legislators.application.use_cases import GetLegislatorVoteAnalyticsUseCase, ImportLegislatorsFromCSVUseCase
from legislators.infrastructure.api.serializers import LegislatorVoteAnalyticsSerializer
from legislators.infrastructure.db.repositories import LegislatorRepository


class LegislatorVoteAnalyticsView(APIView):
  def get(self, request):
    repo = LegislatorRepository()
    use_case = GetLegislatorVoteAnalyticsUseCase(repo)
    legislators = use_case.execute()

    serializer = LegislatorVoteAnalyticsSerializer(legislators, many=True)
    return Response(serializer.data)

  def post(self, request):
    if 'file' not in request.FILES:
      return Response({'message': 'No file provided'}, status=400)

    repo = LegislatorRepository()
    use_case = ImportLegislatorsFromCSVUseCase(repo)
    result = use_case.execute(request.FILES['file'])

    return Response(result, status=201)


class LegislatorAnalyticsExportCSV(APIView):
  def get(self, request):
    repo = LegislatorRepository()
    use_case = GetLegislatorVoteAnalyticsUseCase(repo)
    legislators = use_case.execute()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="legislators-support-oppose-count.csv"'

    writer = csv.writer(response)
    writer.writerow(["id", "name", "num_supported_bills", "num_opposed_bills"])

    for row in legislators:
      writer.writerow((row["legislator"].id, row["legislator"].name, row["supported_bills"], row["opposed_bills"]))

    return response