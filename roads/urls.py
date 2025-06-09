from django.urls import path
from .views import RoadSegmentListCreate, TrafficReadingListCreate, RoadSegmentDetail

urlpatterns = [
    path('roadsegments/', RoadSegmentListCreate.as_view(), name='roadsegment-list'),
    path('readings/', TrafficReadingListCreate.as_view(), name='reading-list'),
    path('roadsegments/<int:pk>/', RoadSegmentDetail.as_view(), name='roadsegment-detail'),

]