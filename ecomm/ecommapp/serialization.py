from pyexpat import model
from django.db.models import fields
from rest_framework import serializers
from .models import Student
from django.shortcuts import get_object_or_404
from rest_framework import status

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields= ('Name','City')