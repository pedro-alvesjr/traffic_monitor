from django.shortcuts import render
from rest_framework import generics
from .models import RoadSegment, TrafficReading
from .serializers import RoadSegmentSerializer, TrafficReadingSerializer
from .permissions import IsAdminOrReadOnly

class RoadSegmentList(generics.ListCreateAPIView):
    queryset = RoadSegment.objects.all()
    serializer_class = RoadSegmentSerializer

class TrafficReadingListCreate(generics.ListCreateAPIView):
    queryset = TrafficReading.objects.all()
    serializer_class = TrafficReadingSerializer
    permission_classes = [IsAdminOrReadOnly]