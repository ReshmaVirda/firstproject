# from django.contrib.auth import authenticate, login, logout
# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import  Response
from rest_framework.views import APIView
# from rest_framework.utils import get_tokens_for_user
from .serializer import RegistrationSerializer
from knox.models import AuthToken
# from rest_framework.simplejwt.tokens import RefreshToken

# Create your views here.


class RegistrationView(APIView):
    def post(self, request):
        # return Response({"status":"success"})
        # print(request.data, "data here")
        serializer = RegistrationSerializer(data=request.data)
        print(serializer, "serializer here")
        if serializer.is_valid():
            user = serializer.save()
            print(user, "user ")
            return Response({"data":serializer.data})
           