from urllib import request, response
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,HttpResponse
from rest_framework import serializers
from ecommapp.serialization import studentserializer
from .models import Student
from rest_framework.decorators import api_view
from rest_framework import viewsets
# Create your views here.


#@api_view(['GET'])
#def studentview(request):
  #if  Student.objects.all():










class student(viewsets.ModelViewSet):
   queryset = Student.objects.all()
   serializer_class = studentserializer