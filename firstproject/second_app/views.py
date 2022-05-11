from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
 

def results(request):
    response="perfect"
    return HttpResponse(response)

