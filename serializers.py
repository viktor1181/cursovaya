from django.shortcuts import render
from rest_framework import serializers
from .models import *


# Create your views here.
class CarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"

class CarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"

class EnginesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engines
        fields = "__all__"


class ModelsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Models
        fields = "__all__"

class ConfigurationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = "__all__"

class TransmissionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transmissions
        fields = "__all__"
class DrivesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drives
        fields = "__all__"