from django.urls import path
from .views import LegislatorVoteStatsView

urlpatterns = [
    path('stats/', LegislatorVoteStatsView.as_view()),
    path('import/', LegislatorVoteStatsView.as_view()),
]