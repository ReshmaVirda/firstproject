from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from .models import Question,Choice
# Create your views here.
def index(request):
   choices = Choice.objects.filter(question_id=1)
   choices1 =Choice.objects.filter()
   return render(request,'firstapp/home.html',{"choices":choices})


def deatil(request,question_id):
    return HttpResponse("looking question %s", question_id)


def results(request,question_id):
    response="looking question %s"
    return HttpResponse(response % question_id)


def vote(request,question_id):
    return HttpResponse("looking question %s", question_id)




    
    #choices 