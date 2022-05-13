from django.urls import path

from . import views
app_name = 'firstapp'

urlpatterns = [
    path('',views.index,name="index"),
    path('detail/<int:pk>',views.deatil,name="detail"),
    path('add/', views.add, name='add'),
    path('update/<int:pk>', views.update, name='update'),
     path('delete/<int:pk>', views.delete, name='delete'),


    # path('results/<int:question_id>',views.results,name="results"),
    # path('vote/<int:question_id>',views.vote,name="vote"),
   # path('add-new/',views.addnew,name="addnew"),
]