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

    def get_intensity(self, obj):
        speed = obj.average_speed

        if speed <= 20:
            return 'elevada'
        elif speed <= 50:
            return 'média'
        return 'baixa'
    