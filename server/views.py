from django.shortcuts import render
from rest_framework import generics
from rest_framework import views
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.http import HttpResponse
from rest_framework import status
from django.core import serializers
import json
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder


# Create your views here.

class EnginesListView(generics.ListAPIView):
    serializer_class = EnginesListSerializer
    queryset = Engines.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        data = serializers.serialize('json', queryset)
        return HttpResponse(data, content_type='application/json')

class TransmissionsListView(generics.ListAPIView):
    serializer_class = TransmissionsListSerializer
    queryset = Transmissions.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        data = serializers.serialize('json', queryset)
        return HttpResponse(data, content_type='application/json')

class DrivesListView(generics.ListAPIView):
    serializer_class = DrivesListSerializer
    queryset = Drives.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        data = serializers.serialize('json', queryset)
        return HttpResponse(data, content_type='application/json')


class ModelsView(views.APIView):

    def get(self, request):
        data = serializers.serialize('json', Models.objects.all())
        return HttpResponse(data, content_type='application/json')

    def post(self, request):
        serializer = ModelsListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data, status=status.HTTP_201_CREATED)
        return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ModelsViewDelete(views.APIView):

    def get_object(self, pk):
        try:
            return Models.objects.get(pk=pk)
        except Models.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        model = self.get_object(pk)
        serializer = ModelsListSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data)
        return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        model = self.get_object(pk)
        model.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class ConfigurationView(views.APIView):

    def get(self, request):
        data = serializers.serialize('json', Configuration.objects.all(),
                                     indent=3,
                                     use_natural_foreign_keys=True,
                                     use_natural_primary_keys=True
                                     )
        # data = serializers.CharField(source="engine.nameEngine")
        return HttpResponse(data, content_type='application/json')

    def post(self, request):
        serializer = ConfigurationListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data, status=status.HTTP_201_CREATED)
        return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConfigurationViewDelete(views.APIView):

    def get_object(self, pk):
        try:
            return Configuration.objects.get(pk=pk)
        except Configuration.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        model = self.get_object(pk)
        serializer = ConfigurationListSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data)
        return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        model = self.get_object(pk)
        model.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
