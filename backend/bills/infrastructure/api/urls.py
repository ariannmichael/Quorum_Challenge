from django.urls import path
from bills.infrastructure.api.views import BillStatsAPIView

urlpatterns = [
    path('stats/', BillStatsAPIView.as_view()),
    path('import/', BillStatsAPIView.as_view()),
]