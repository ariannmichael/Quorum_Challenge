from django.urls import path
from .views import LegislatorVoteAnalyticsView

urlpatterns = [
    path('analytics/', LegislatorVoteAnalyticsView.as_view()),
    path('import/', LegislatorVoteAnalyticsView.as_view()),
]