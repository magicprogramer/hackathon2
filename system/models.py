from django.db import models

# Create your models here.
class Zone(models.Model):
    location = models.CharField(max_length=5)
    needMaintanance = models.BooleanField(default=False)
    last_maintanace = models.DateTimeField()
class Dragon(models.Model):
    zone = models.ForeignKey(Zone, related_name="dragon", on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    digest_period = models.IntegerField()
    herbivore = models.BooleanField()
    last_meal = models.DateTimeField()
