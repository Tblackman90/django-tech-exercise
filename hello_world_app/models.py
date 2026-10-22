from django.db import models

# saves motorcycle maintenance info
class Maintenance(models.Model):
    service = models.CharField(max_length=100)
    date = models.DateField()
    mileage = models.IntegerField()
    notes = models.TextField(blank=True)
