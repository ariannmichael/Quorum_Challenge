from rest_framework.views import APIView
from rest_framework.response import Response

from votes.infrastructure.db.repositories import VotesRepository
from votes.application.use_cases import ImportVotesUseCase

class VotesAPIView(APIView):
    def post(self, request):
        if 'file' not in request.FILES:
            return Response({'message': 'No file provided'}, status=400)

        repo = VotesRepository()
        use_case = ImportVotesUseCase(repo)
        result = use_case.execute(request.FILES['file'])

        return Response(result, status=201)