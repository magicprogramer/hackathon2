from django.db.models.signals import post_save
from .models import *
def update_zone_carnivore_count(sender, instance, **kwargs):
    instance.zone.update_carnivore_count()

post_save.connect(update_zone_carnivore_count, sender=Dragon)