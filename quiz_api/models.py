from django.db import models
from datetime import datetime,timedelta
from django.utils import timezone

# Create your models here.
class QuizModel(models.Model):
    question = models.CharField(max_length=250)
    choices = models.ManyToManyField('Choice')
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    active = models.BooleanField(default=False)
    result = models.CharField(max_length=10,null=True)

    def is_result_available(self):
        current_time = timezone.now()
        result_available_time = self.endDate + timedelta(minutes=5)
        return current_time >= result_available_time


    # def save(self, *args, **kwargs):
    #     if not self.id:  
    #         self.startDate = datetime.now()
    #         self.endDate = datetime.now()
    #     return super(QuizModel, self).save(*args, **kwargs)

class Choice(models.Model):
    question = models.ForeignKey(QuizModel,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=50)
    is_correct = models.BooleanField(default=False)

