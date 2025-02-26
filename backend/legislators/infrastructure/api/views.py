from rest_framework.views import APIView
from rest_framework.response import Response

from legislators.application.use_cases import GetLegislatorsUseCase
from legislators.infrastructure.api.serializers import LegislatorSerializer
from legislators.infrastructure.db.repositories import LegislatorRepository


class LegislatorListView(APIView):
  def get(self, request):
    repo = LegislatorRepository()
    use_case = GetLegislatorsUseCase(repo)
    legislators = use_case.execute()

    serializer = LegislatorSerializer(legislators, many=True)
    return Response(serializer.data)