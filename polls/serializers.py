
from .models import Poll
from rest_framework import serializers


class PollSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Poll
        fields = ['name', 'date_start', 'date_end', 'description', 'questions',]