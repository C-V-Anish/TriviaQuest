from django.urls import path,include
from .views import CreateQuiz,ActiveQuiz,ResultQuiz,AllQuiz

urlpatterns = [
    path('',CreateQuiz.as_view(),name="create-quiz"),
    path('active/',ActiveQuiz.as_view(),name='active-quiz'),
    path('<int:pk>/result/',ResultQuiz.as_view(),name='result-quiz'),
    path('all/',AllQuiz.as_view(),name='all-quiz'),
]
