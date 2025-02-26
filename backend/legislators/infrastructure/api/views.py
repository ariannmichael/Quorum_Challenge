from rest_framework.views import APIView
from rest_framework.response import Response

from legislators.application.use_cases import GetLegislatorVoteAnalyticsUseCase, ImportLegislatorsFromCSVUseCase
from legislators.infrastructure.api.serializers import LegislatorVoteAnalyticsSerializer
from legislators.infrastructure.db.repositories import LegislatorRepository
from legislators.application.tasks import import_legislators_from_csv_task

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