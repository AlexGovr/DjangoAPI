
from .models import Poll, Question
from rest_framework import serializers


class PollSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll
        fields = ['name', 'date_start', 'date_end', 'description', 'questions', 'id']

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['text', 'question_type', 'id']