from django.urls import path
from .views import VoteResultsAPIView

urlpatterns = [
    path('import/', VoteResultsAPIView.as_view())
]

