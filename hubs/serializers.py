from rest_framework import serializers
from .models import LearningHub

class LearningHubSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningHub
        fields = "__all__"