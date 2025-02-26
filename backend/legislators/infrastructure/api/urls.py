from django.urls import path
from .views import LegislatorVoteStatsView

urlpatterns = [
    path('legislators/stats/', LegislatorVoteStatsView.as_view()),
    path('legislators/import/', LegislatorVoteStatsView.as_view()),
]