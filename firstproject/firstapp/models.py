from django.db import models

# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=50)
    pub_date=models.DateTimeField(auto_now_add=True, blank=True)


    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=100)
    vote=models.IntegerField(default=0)
    