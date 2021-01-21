from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Poll, Question
from .serializers import PollSerializer, QuestionSerializer


class BasicViewSet(viewsets.ModelViewSet):
    def not_auth(self):
        return Response({'status': 'rejected: not authenticated'})

    def get_instance(self, id_):
        return self.queryset(id=id_)

class PollViewSet(BasicViewSet):
    """
    API endpoint that allows polls to be viewed or edited
    """
    queryset = Poll.objects.all().order_by('-date_start', ).reverse()
    serializer_class = PollSerializer

class PollEditViewSet(PollViewSet):
    
    @action(detail=False, url_path='save', methods=['get', 'post'])
    def save(self, request):
        if not request.user.is_authenticated:
            return self.not_auth()

        poll = self.get_instance(int(request.data['id']))
        srl = self.serializer_class(instance=poll, data=request.data)
        srl.is_valid(raise_exception=True)
        srl.save()
        context = {'status': 'poll editing successful'}
        return Response(context)

    @action(detail=False, url_path='create', methods=['get', 'post'])
    def create_poll(self, request):
        if not request.user.is_authenticated:
            return self.not_auth()
        
        srl = self.serializer_class(data=request.data)
        srl.is_valid(raise_exception=True)
        new_poll = srl.save()
        context = {'status': 'poll created successfuly', 'poll_id': f'{new_poll.id}'}
        return Response(context)

    @action(detail=False, url_path='delete', methods=['get', 'post'])
    def delete_poll(self, request):
        if not request.user.is_authenticated:
            return self.not_auth()
        
        poll = self.get_instance(int(request.data['id']))
        poll.delete()
        context = {'status': 'poll deleted successfuly'}
        return Response(context)

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

