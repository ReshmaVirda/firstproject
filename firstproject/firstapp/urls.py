from django.urls import path

from . import views

urlpatterns = [
    path('index/',views.index,name="index"),
    path('detail/<int:question_id>',views.deatil,name="detail"),
    path('results/<int:question_id>',views.results,name="results"),
    path('vote/<int:question_id>',views.vote,name="vote"),
]