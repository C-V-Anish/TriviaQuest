from rest_framework import serializers
from .models import QuizModel,Choice

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['choice_text','is_correct']

class QuizModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizModel
        fields = ["question","choices","startDate","endDate","active","result"]

    def create(self, validated_data):
        choices_data = validated_data.pop('choices')
        quiz = QuizModel.objects.create(**validated_data)

        for choice_data in choices_data:
            Choice.objects.create(quiz=quiz, **choice_data)

        return quiz
    

