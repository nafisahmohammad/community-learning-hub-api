from django.db import models
from django.conf import settings
from hubs.models import LearningHub

class Course(models.Model):
    class Level(models.TextChoices):
        BEGINNER = "BEGINNER", "Beginner"
        INTERMEDIATE = "INTERMEDIATE", "Intermediate"

    title = models.CharField(max_length=140)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=80, blank=True)
    level = models.CharField(max_length=20, choices=Level.choices, default=Level.BEGINNER)
    hub = models.ForeignKey(LearningHub, on_delete=models.CASCADE, related_name="courses")
    mentor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="mentored_courses"
    )
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
