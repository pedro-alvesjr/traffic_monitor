from rest_framework import serializers
from .models import RoadSegment, TrafficReading

class RoadSegmentSerializer(serializers.ModelSerializer):
    total_readings = serializers.SerializerMethodField()
    
    class Meta:
        model = RoadSegment
        fields = ['id', 'name', 'geometry', 'created_at', 'total_readings']

    def get_total_readings(self, obj):
        return obj.readings.count()

class TrafficReadingSerializer(serializers.ModelSerializer):
    intensity = serializers.SerializerMethodField()

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
    