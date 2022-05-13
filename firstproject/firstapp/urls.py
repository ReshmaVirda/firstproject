from django.urls import path

from . import views
app_name = 'firstapp'

urlpatterns = [
    path('',views.index,name="index"),
    path('detail/<int:pk>',views.deatil,name="jamil"),
    path('add/', views.add, name='add'),
    


    # path('results/<int:question_id>',views.results,name="results"),
    # path('vote/<int:question_id>',views.vote,name="vote"),
   # path('add-new/',views.addnew,name="addnew"),
]