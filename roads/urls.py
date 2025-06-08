from django.urls import path
from .views import RoadSegmentList, TrafficReadingListCreate

urlpatterns = [
    path('roadsegments/', RoadSegmentList.as_view(), name='roadsegment-list'),
    path('readings/', TrafficReadingListCreate.as_view(), name='reading-list')
]