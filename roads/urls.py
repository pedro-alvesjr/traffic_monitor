from django.urls import path
from .views import RoadSegmentList

urlpatterns = [
    path('roadsegments/', RoadSegmentList.as_view(), name='roadsegment-list')
]