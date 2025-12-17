from django.urls import path
from .views import LegislatorVoteAnalyticsView, LegislatorAnalyticsExportCSV

urlpatterns = [
    path('analytics/', LegislatorVoteAnalyticsView.as_view()),
    path('import/', LegislatorVoteAnalyticsView.as_view()),
    path('export/', LegislatorAnalyticsExportCSV.as_view()),
]

