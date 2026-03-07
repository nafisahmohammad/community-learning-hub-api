from rest_framework import viewsets
from .models import LearningHub
from .serializers import LearningHubSerializer

class LearningHubViewSet(viewsets.ModelViewSet):
    queryset = LearningHub.objects.all()
    serializer_class = LearningHubSerializer
