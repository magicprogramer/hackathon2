from rest_framework import serializers
from .models import *
class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = ["pk", "dragon", "location", "last_maintanace", "needMaintanance", "number_of_carnivors"]
class DragonsSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Dragon
        fields = "__all__"
