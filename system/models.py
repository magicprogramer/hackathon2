from django.db import models

# Create your models here.
class Zone(models.Model):
    location = models.CharField(max_length=5)
    needMaintanance = models.BooleanField(default=False)
    last_maintanace = models.DateTimeField()
    number_of_carnivors = models.PositiveBigIntegerField(default=0)
    def __str__(self):
        return self.location
    
    
    def update_carnivore_count(self):
        carnivore_count = Dragon.objects.filter(Zone=self, herbivore='True').count()
        self.number_of_carnivors = carnivore_count
        self.save()



class Dragon(models.Model):
    zone = models.ForeignKey(Zone, related_name="dragon", on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    digest_period = models.IntegerField()
    herbivore = models.BooleanField()
    last_meal = models.DateTimeField()
    name = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.name} in {self.zone.location}"
class Maintain_record(models.Model):
    date = models.DateTimeField()
    Zone = models.ForeignKey(Zone, related_name= "maintains", on_delete=models.CASCADE)
