from django.urls import path

from . import views

urlpatterns = [

    path('hello',views.results,name="results"),



]