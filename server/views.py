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
    context_object_name = 'models'  # ваше собственное имя переменной контекста в шаблоне
    #template_name = 'index.html'  # Определение имени вашего шаблона и его расположения

    def list(self, request):
        queryset = self.get_queryset()
        serializer = EnginesListSerializer(queryset, many=True)
        #return render(request, 'server/index.html', {'models': queryset})
        data = serializers.serialize('json', queryset)
        return HttpResponse(data, content_type='application/json')

class TransmissionsListView(generics.ListAPIView):
    serializer_class = TransmissionsListSerializer
    queryset = Transmissions.objects.all()
    #context_object_name = 'models'  # ваше собственное имя переменной контекста в шаблоне
    #template_name = 'index.html'  # Определение имени вашего шаблона и его расположения

    def list(self, request):
        queryset = self.get_queryset()
        serializer = TransmissionsListSerializer(queryset, many=True)
        #return render(request, 'server/index.html', {'models': queryset})
        data = serializers.serialize('json', queryset)
        return HttpResponse(data, content_type='application/json')

class DrivesListView(generics.ListAPIView):
    serializer_class = DrivesListSerializer
    queryset = Drives.objects.all()
    #context_object_name = 'models'  # ваше собственное имя переменной контекста в шаблоне
    #template_name = 'index.html'  # Определение имени вашего шаблона и его расположения

    def list(self, request):
        queryset = self.get_queryset()
        serializer = DrivesListSerializer(queryset, many=True)
        #return render(request, 'server/index.html', {'models': queryset})
        data = serializers.serialize('json', queryset)
        return HttpResponse(data, content_type='application/json')

class ModelsView(views.APIView):

    def get(self, request):
        queryset = Models.objects.all()
        serializer = ModelsListSerializer(queryset, many=True)
        #return render(request, 'server/index.html', {'models': queryset})
        #return HttpResponse(serializer.data)
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
        queryset = Configuration.objects.all()
        #serializer = ConfigurationListSerializer(queryset, many=True)
        serialized_instance = serializers.serialize('json', [queryset, ])
        #return render(request, 'server/index.html', {'models': queryset})
        #return HttpResponse(serializer.data)
        #dict_obj = model_to_dict(queryset)
        #serialized = json.dumps(list(dict_obj), cls=DjangoJSONEncoder)
        #return HttpResponse(serialized, content_type="application/json")
        data = serializers.serialize('json', Configuration.objects.all(), fields=(engine,transmission,drive,model))
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
        #serializer = ConfigurationListSerializer(model, data=request.data)
        serialized_instance = serializers.serialize('json', [model, ])
        if serializer.is_valid():
            serializer.save()
            #return HttpResponse(serializer.data)
            return HttpResponse(serialized_instance, content_type="application/json")
        return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        model = self.get_object(pk)
        model.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

