from rest_framework import serializers
from .models import QuizModel,Choice

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id','choice_text','is_correct']

class QuizModelSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)
    class Meta:
        model = QuizModel
        fields = ["question","choices","startDate","endDate","active","result"]

    def create(self, validated_data):
        choices_data = validated_data.pop('choices')
        quiz = QuizModel.objects.create(**validated_data)

        for choice_data in choices_data:
            choice_serializer = ChoiceSerializer(data=choice_data)
            choice_serializer.is_valid(raise_exception=True)
            choice = choice_serializer.save(question=quiz)
            quiz.choices.add(choice)

        return quiz
    

