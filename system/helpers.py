from .models import *
def updatezones(zoneid):
    zone = Zone.objects.get(pk=zoneid)
    dragons = Dragon.objects.filter(zone = zone, herbivore = False).count()
    zone.number_of_carnivors = dragons
    zone.save()