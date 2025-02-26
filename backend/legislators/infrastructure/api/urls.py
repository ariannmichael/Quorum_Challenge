from django.urls import path
from .views import LegislatorListView

urlpatterns = [
    path('legislators/', LegislatorListView.as_view(), name='legislator-list')
]