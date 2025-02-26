from rest_framework.views import APIView
from rest_framework.response import Response

from legislators.application.use_cases import GetLegislatorVoteStatsUseCase, ImportLegislatorsFromCSVUseCase
from legislators.infrastructure.api.serializers import LegislatorVoteStatsSerializer
from legislators.infrastructure.db.repositories import LegislatorRepository
from legislators.application.tasks import import_legislators_from_csv_task

class LegislatorVoteStatsView(APIView):
  def get(self, request):
    repo = LegislatorRepository()
    use_case = GetLegislatorVoteStatsUseCase(repo)
    legislators = use_case.execute()

    serializer = LegislatorVoteStatsSerializer(legislators, many=True)
    return Response(serializer.data)

  def post(self, request):
    if 'file' not in request.FILES:
      return Response({'message': 'No file provided'}, status=400)

    # csv_file_data = request.FILES['file'].read().decode('utf-8')
    #
    # import_legislators_from_csv_task.delay(csv_file_data)

    repo = LegislatorRepository()
    use_case = ImportLegislatorsFromCSVUseCase(repo)
    result = use_case.execute(request.FILES['file'])

    return Response(result, status=201)