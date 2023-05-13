from rest_framework import serializers
from .models import QuizModel,Choice

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['choice_text','is_correct']

class QuizModelSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    class Meta:
        model = QuizModel
        fields = '__all__'

    def create(self, validated_data):
        options_data = validated_data.pop('options')
        quiz = QuizModel.objects.create(**validated_data)

        for option_data in options_data:
            Choice.objects.create(quiz=quiz, **option_data)

        return quiz
    

