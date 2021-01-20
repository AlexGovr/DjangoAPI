from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Poll
from .serializers import PollSerializer


class PollViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows polls to be viewed or edited
    """
    queryset = Poll.objects.all().order_by('-date_start', ).reverse()
    serializer_class = PollSerializer