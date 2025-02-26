from django.urls import path
from bills.infrastructure.api.views import BillAnalyticsAPIView

urlpatterns = [
    path('analytics/', BillAnalyticsAPIView.as_view()),
    path('import/', BillAnalyticsAPIView.as_view()),
]