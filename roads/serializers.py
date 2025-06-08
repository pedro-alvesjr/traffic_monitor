from rest_framework import serializers
from .models import RoadSegment, TrafficReading

class RoadSegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadSegment
        fields = '__all__'

class TrafficReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrafficReading
        fields = '__all__'