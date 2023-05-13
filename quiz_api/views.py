from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView
from .serializers import QuizModelSerializer
from rest_framework import permissions
from .models import QuizModel
from datetime import datetime
# Create your views here.

permission_classes=(permissions.IsAuthenticated,)

class CreateQuiz(CreateAPIView):
    serializer_class =  QuizModelSerializer
    permission_classes = permission_classes

    def perform_create(self, serializer):
        serializer.save()

class ActiveQuiz(ListAPIView):
    serializer_class =  QuizModelSerializer
    permission_classes = permission_classes

    def get_queryset(self):
        current_time = datetime.now()
        return QuizModel.objects.filter(startDate=current_time,endData=current_time,is_active=True)

class AllQuiz(ListAPIView):
    serializer_class =  QuizModelSerializer
    permission_classes = permission_classes

    def get_queryset(self):
        return QuizModel.objects.all()
    
class ResultQuiz(RetrieveAPIView):
    serializer_class =  QuizModelSerializer
    permission_classes = permission_classes

    def get_queryset(self):
        return QuizModel.objects.all()
    