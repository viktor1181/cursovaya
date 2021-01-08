from django.shortcuts import render
from rest_framework import serializers
from .models import *
from django.core.serializers.json import Serializer
from io import StringIO
from django.core.serializers.json import Serializer as JsonSerializer
from django.core.serializers.python import Serializer as PythonSerializer
from django.core.serializers.base import Serializer as BaseSerializer
# Create your views here.

class ExtBaseSerializer(BaseSerializer):
    def serialize(self, queryset, **options):
        self.selected_props = options.pop('props')
        return super(ExtBaseSerializer, self).serialize(queryset, **options)

    def serialize_property(self, obj):
        model = type(obj)
        for field in self.selected_props:
            if hasattr(model, field) and type(getattr(model, field)) == property:
                self.handle_prop(obj, field)

    def handle_prop(self, obj, field):
        self._current[field] = getattr(obj, field)

    def end_object(self, obj):
        self.serialize_property(obj)

        super(ExtBaseSerializer, self).end_object(obj)

class ExtPythonSerializer(ExtBaseSerializer, PythonSerializer):
    pass

class ExtJsonSerializer(ExtPythonSerializer, JsonSerializer):
    pass


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