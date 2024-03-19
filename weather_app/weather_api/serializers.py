from rest_framework import serializers
from .models import DayTemp

class DayTempSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayTemp
        fields = "__all__"
