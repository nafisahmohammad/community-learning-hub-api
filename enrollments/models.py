from django.db import models
from django.conf import settings
from courses.models import Course

class Enrollment(models.Model):
    class Status(models.TextChoices):
        ENROLLED = "ENROLLED", "Enrolled"
        COMPLETED = "COMPLETED", "Completed"
        DROPPED = "DROPPED", "Dropped"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="enrollments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ENROLLED)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "course"], name="unique_user_course_enrollment")
        ]

    def __str__(self):
        return f"{self.user.email} -> {self.course.title}"