from django.shortcuts import render
from rest_framework import generics
from .models import RoadSegment
from .serializers import RoadSegmentSerializer

class RoadSegmentList(generics.ListCreateAPIView):
    queryset = RoadSegment.objects.all()
    serializer_class = RoadSegmentSerializer