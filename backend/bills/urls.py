from django.urls import path
from .views import BillAnalyticsAPIView, BillAnalyticsExportCSV

urlpatterns = [
    path('analytics/', BillAnalyticsAPIView.as_view()),
    path('import/', BillAnalyticsAPIView.as_view()),
    path('export/', BillAnalyticsExportCSV.as_view()),
]

