from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView
from .serializers import QuizModelSerializer
from rest_framework import permissions
from .models import QuizModel
from datetime import datetime,timezone
from rest_framework.response import Response
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

    def check_current_time(self):
        current_date = datetime.now().date()
        current_time = datetime.now().time()
        # print(f"{current_date},{current_time}")
        quizzes =QuizModel.objects.all()

        for quiz in quizzes:
            # print(f"{quiz.startDate.date()},{quiz.startDate.time()},{quiz.endDate.time()}")
            if quiz.startDate.date() == current_date and (quiz.startDate.time() <= current_time <= quiz.endDate.time()):
                quiz.active = True
                quiz.save()
            else:
                quiz.active = False
                quiz.save()

    
    def get_queryset(self):
        self.check_current_time()
        return QuizModel.objects.filter(active = True)

class AllQuiz(ListAPIView):
    serializer_class =  QuizModelSerializer
    permission_classes = permission_classes

    def get_queryset(self):
        return QuizModel.objects.all()
    
class ResultQuiz(RetrieveAPIView):
    serializer_class =  QuizModelSerializer
    permission_classes = permission_classes

    def get_queryset(self):
        quiz_id = self.kwargs['pk']
        quiz = QuizModel.objects.filter(id = quiz_id)
        return quiz

    def retrieve(self, request, *args, **kwargs):
        quiz = self.get_object()
        return self.view_result(quiz)

    def view_result(self, quiz):
        if quiz.is_result_available():
            right_answer = quiz.choices.filter(is_correct=True).values_list('choice_text', flat=True)
            response_data = {
                "question": quiz.question,
                "answer": list(right_answer)
            }
            return Response(response_data)
        else:
            return Response({"message": "Quiz result is not available yet."}, status=400)
    