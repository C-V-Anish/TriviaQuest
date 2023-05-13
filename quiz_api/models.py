from django.db import models
from datetime import datetime

# Create your models here.
class QuizModel(models.Model):
    question = models.CharField(max_length=250)
    options = models.ManyToManyField('Choice')
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    is_active = models.BooleanField(default=False)
    result = models.CharField(max_length=10)

class Choice(models.Model):
    question = models.ForeignKey(QuizModel,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=50)
    is_corrext = models.BooleanField(default=False)