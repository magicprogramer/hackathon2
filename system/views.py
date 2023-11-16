from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, filters
from .serializers import *
from .helpers import *
@api_view(["GET", "POST"])
def ListZone(request):
    if request.method == "GET":
        zones = Zone.objects.all()
        serializer = ZoneSerializer(zones, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ZoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
@api_view(["GET"])
def retrive(request, pk):
    if request.method == 'GET':
        zone = Zone.objects.get(pk=pk)
        serializer = ZoneSerializer(zone)
        return Response(serializer.data, status=status.HTTP_200_OK)
@api_view(["GET"])
def move(request, pk, newzone):
    if request.method=="GET":
        try :
            dragon = Dragon.objects.get(pk=pk)
            newzone = Zone.objects.get(pk = newzone)
            old= dragon.zone.id
            dragon.zone = newzone
            dragon.save()
            news = dragon.zone.id
            updatezones(old)
            updatezones(news)
            serializer = DragonsSerilizer(dragon)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except dragon.DoesNotExist or newzone.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    