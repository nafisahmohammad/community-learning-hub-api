from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    hub_name = serializers.CharField(source="hub.name", read_only=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "description",
            "category",
            "level",
            "hub",
            "hub_name",
            "mentor",
            "is_published",
        ]