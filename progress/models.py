from django.db import models
from enrollments.models import Enrollment

class ProgressTracking(models.Model):
    enrollment = models.OneToOneField(Enrollment, on_delete=models.CASCADE, related_name="progress")
    percent_complete = models.PositiveSmallIntegerField(default=0)
    last_activity_at = models.DateTimeField(null=True, blank=True)
    last_synced_at = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Progress {self.enrollment_id}: {self.percent_complete}%"
