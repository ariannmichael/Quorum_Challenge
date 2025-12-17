from django.urls import path
from .views import VotesAPIView

urlpatterns = [
    path('import/', VotesAPIView.as_view())
]

