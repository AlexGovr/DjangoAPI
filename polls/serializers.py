
from .models import Poll, Question, FinishedPoll, Answer
from rest_framework import serializers


class PollSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll
        fields = ['name', 'date_start', 'date_end', 'description', 'questions', 'id']


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['text', 'question_type', 'id']


class FinishedPollSerializer(serializers.ModelSerializer):

    class Meta:
        model = FinishedPoll
        fields = ['user_id', 'poll', 'id']


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['text', 'question', 'id', 'finished_poll']