from django.db import models

class LearningHub(models.Model):
    name = models.CharField(max_length=120)
    country = models.CharField(max_length=80)
    state = models.CharField(max_length=80, blank=True)
    city = models.CharField(max_length=80)
    address = models.CharField(max_length=200, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.city}"