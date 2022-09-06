from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    #path('signup',views.Signup),
    path('api/register/', views.RegisterPI.as_view()),
   #path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]