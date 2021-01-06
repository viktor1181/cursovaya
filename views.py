from django.shortcuts import render
from rest_framework import generics
from rest_framework import views
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.http import HttpResponse
from rest_framework import status

# Create your views here.
class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer


class CarListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()


class EnginesListView(generics.ListAPIView):
    serializer_class = EnginesListSerializer
    queryset = Engines.objects.all()
    context_object_name = 'models'  # ваше собственное имя переменной контекста в шаблоне
    #template_name = 'index.html'  # Определение имени вашего шаблона и его расположения

    def list(self, request):
        queryset = self.get_queryset()
        serializer = EnginesListSerializer(queryset, many=True)
        #return render(request, 'server/index.html', {'models': queryset})
        return HttpResponse(serializer.data)

class TransmissionsListView(generics.ListAPIView):
    serializer_class = TransmissionsListSerializer
    queryset = Transmissions.objects.all()
    #context_object_name = 'models'  # ваше собственное имя переменной контекста в шаблоне
    #template_name = 'index.html'  # Определение имени вашего шаблона и его расположения

    def list(self, request):
        queryset = self.get_queryset()
        serializer = TransmissionsListSerializer(queryset, many=True)
        #return render(request, 'server/index.html', {'models': queryset})
        return HttpResponse(serializer.data)

class DrivesListView(generics.ListAPIView):
    serializer_class = DrivesListSerializer
    queryset = Drives.objects.all()
    #context_object_name = 'models'  # ваше собственное имя переменной контекста в шаблоне
    #template_name = 'index.html'  # Определение имени вашего шаблона и его расположения

    def list(self, request):
        queryset = self.get_queryset()
        serializer = DrivesListSerializer(queryset, many=True)
        #return render(request, 'server/index.html', {'models': queryset})
        return HttpResponse(serializer.data)

class ModelsView(views.APIView):

    def get(self, request):
        queryset = Models.objects.all()
        serializer = ModelsListSerializer(queryset, many=True)
        #return render(request, 'server/index.html', {'models': queryset})
        return HttpResponse(serializer.data)

    def post(self, request):
        serializer = ModelsListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        model = self.get_object(pk)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ConfigurationView(views.APIView):

    def get(self, request):
        queryset = Configuration.objects.all()
        serializer = ConfigurationListSerializer(queryset, many=True)
        #return render(request, 'server/index.html', {'models': queryset})
        return HttpResponse(serializer.data)

    def post(self, request):
        serializer = ConfigurationListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        model = self.get_object(pk)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

