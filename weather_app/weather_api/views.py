from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from . import meteo
from .models import DayTemp
from .serializers import DayTempSerializer

# Create your views here.

def queryDataFromMeteo(request)-> JsonResponse:
    data = meteo.getMeteoTruncated()
    return JsonResponse(data, safe=False)

@api_view(['GET'])
def listDayTempData(request):
    data = DayTemp.objects.all()
    serializer = DayTempSerializer(data, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def storeDayTempData(request):
    # todo detect if object was not saved because it already exists.
    serializer = None
    if isinstance(request.data, list):
        serializer = DayTempSerializer(data = request.data, many=True)
    else:
        serializer = DayTempSerializer(data = request.data, many=False)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def readDayTempData(request, id):
    data = DayTemp.objects.filter(id=id).first()
    if data is not None:
        serializer = DayTempSerializer(data, many = False)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def updateDayTempData(request, id):
    item = DayTemp.objects.get(id=id)
    serializer = DayTempSerializer(instance = item, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteDayTempData(request, id):
    if id == 0:
        DayTemp.objects.all().delete()
    else:
        DayTemp.objects.get(id=id).delete()
    return Response()