from rest_framework.views import APIView
from rest_framework.response import Response

from vote_results.infrastructure.db.repositories import VoteResultsRepository
from vote_results.application.use_cases import ImportVoteResultsUseCase

class VoteResultsAPIView(APIView):
    def post(self, request):
        if 'file' not in request.FILES:
            return Response({'message': 'No file provided'}, status=400)

        repo = VoteResultsRepository()
        use_case = ImportVoteResultsUseCase(repo)
        result = use_case.execute(request.FILES['file'])

        return Response(result, status=201)