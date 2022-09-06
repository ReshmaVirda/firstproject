from typing_extensions import Self
from urllib import request, response
from venv import create
from xmlrpc.client import ResponseError
from django.shortcuts import render


from rest_framework.permissions import IsAuthenticated
from .models import Sign_Up,Sign_in,Forgot_Password
from .serializer import SignupSerializer,SigninSerializer,ForgotpasswordSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import generics,permissions
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
# Create your views here.
# # Class based view to Get User Details using Token Authentication
# class RegisterAPI(APIView):
#   authentication_classes = (TokenAuthentication,)
#   permission_classes = (AllowAny,)
#   def get(self,request,*args,**kwargs):

#     user = Sign_Up.objects.get(id=request.user.id)
#     serializer = SignupSerializer(user)
#     return Response(serializer.data)

class RegisterPI(APIView):
    """ 
    Creates the user. 
    """

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response({"status":"Success", "data":serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




















# class SignupAPIView(APIView):
#     def post(self,request):
#         searializer =  SignupSerializer(data=request.data)
#         searializer.is_valid()
#         searializer.save()
#         return response(searializer.data)





# @api_view(['POST'])   #'GET','DELETE'
# def Signup(request):
#     if request.method == "POST":
#         signup_data = JSONParser().parse(request)
#         signup_serializer = SignupSerializer(data=signup_data)
#         if signup_serializer.is_valid():
#             signup_serializer.save()
#             return JsonResponse(signup_serializer.data, status=status.HTTP_201_CREATED) 
#         return JsonResponse(signup_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class Sign_UpCreateApi(generics.CreateAPIView):
#      permission_classes = (IsAuthenticated,)   

#      queryset = Sign_Up.objects.all()
#      serializer_class = SignupSerializer



    # def post(self, request):
    #   serializer = SignupSerializer(data=request.data)
    #   if serializer.is_valid():
    #       Sign_Up(
    #         serializer.save()
    #     )
    #   return response({"status":"sucess", "code":status.HTTP_201_CREATED, "details":serializer.data})
    #   return Response({"status":"unsuccessful", "code":status.HTTP_400_BAD_REQUEST, "detsils":serializer.errors})

# @api_view(['PUT'])   #'GET','DELETE'
# def Signup_detail(request,pk):
#     try: 
#         students = Sign_Up.objects.get(pk=pk) 
#     except Sign_Up.DoesNotExist: 
#         return JsonResponse({'message': 'The Student does not exist'}, status=status.HTTP_404_NOT_FOUND) 

#     if request.method == 'PUT': 
#         student_data = JSONParser().parse(request) 
#         student_serializer = StudentSerializer(students, data=student_data) 
#         if student_serializer.is_valid(): 
#             student_serializer.save() 
#             return JsonResponse(student_serializer.data) 
#         return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

