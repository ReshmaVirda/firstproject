from urllib import request, response
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse
from rest_framework import serializers
from ecommapp.serialization import studentserializer
from .models import Student
from rest_framework.decorators import api_view
from rest_framework import viewsets
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
# Create your views here.


@api_view(['GET','POST','DELETE'])
def studentlist(request):
  if  request.method == 'GET':
    student_list = Student.objects.all()
    student_serializer = studentserializer(student_list, many=True)
    return JsonResponse(student_serializer.data, safe=False)


  elif request.method == 'POST':
        student_data = JSONParser().parse(request)
        student_serializer = student_serializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse(student_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
        count = Student.objects.all().delete()
        return JsonResponse({'message': '{} Students were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


 






# class studentdene(request):
#   s1=
#   s2=