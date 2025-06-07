from django.db import models

class RoadSegment(models.Model):
    name = models.CharField(max_length=100)
    geometry = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TrafficReading(models.Model):
    Road_Segment = models.ForeignKey(RoadSegment, on_delete=models.CASCADE, related_name='readings')
    average_speed = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.Road_Segment.name} - {self.average_speed} km/h'