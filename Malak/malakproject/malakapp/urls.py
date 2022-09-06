# from django.contrib import admin
from django.urls import path
from .views import RegistrationView
# from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    #path('signup',views.Signup),
    path('api/register/', RegistrationView.as_view(),name='register'),
    # path('api/login/', views.LoginAPI.as_view()),
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]