from urllib import response
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Question,Choice
# Create your views here.
def index(request):
   question_list = Question.objects.all()
   output = ', '.join([q.question_text for q in question_list])
   return render(request, 'firstapp/post_list.html', {"question_list":question_list})

def deatil(request,pk):
    choices = Choice.objects.filter(question_id=pk)
    return render(request,'firstapp/detail.html',{"choices":choices, "question_id":pk})


from django.urls import reverse
from django.template import loader
from django.http import HttpResponseRedirect
def add(request):
  if request.method != "POST":
    template = loader.get_template('firstapp/add.html')
    return HttpResponse(template.render({}, request))
  else:
    Question.objects.create(
      question_text=request.POST['first']
      
      )
    return HttpResponseRedirect(reverse('firstapp:index', ))


def update(request,pk):
   if request.method != "POST":
     question = Question.objects.get(id=pk)
     template = loader.get_template('firstapp/update.html')

     return HttpResponse(template.render({"question":question}, request))

   else:
        question = Question.objects.get(id=pk)
        question.question_text = request.POST['question_text']
        question.save()
       
        return HttpResponseRedirect(reverse('firstapp:index', ))


def delete(requset,pk):
  deletelist = Question.objects.get(id=pk)
  deletelist.delete()
  return HttpResponseRedirect(reverse('firstapp:index', ))
        
   





  





# def results(request,question_id):
#     response="looking question %s"
#     return HttpResponse(response % question_id)


# def vote(request,question_id):
#     return HttpResponse("looking question %s", question_id)




    
    #choices 