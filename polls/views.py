from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Poll
from .serializers import PollSerializer


class PollViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows polls to be viewed or edited
    """
    queryset = Poll.objects.all().order_by('-date_start', ).reverse()
    serializer_class = PollSerializer
    
class PollEditViewSet(PollViewSet):
    
    @action(detail=False, url_path='save', methods=['get', 'post'])
    def save(self, request):
        # if request
        print('yaaaaay')
        print(request.data)
        srl = self.serializer_class(data=request.data)
        srl.is_valid(raise_exception=True)
        print(srl.validated_data)
        srl.save()
        context = {'status': 'poll editing successful'}
        return Response(context)

    def post(self, request):
        # if request
        srl = self.serializer_class(data=request.data)
        srl.is_valid(raise_exception=True)
        srl.save()
        context = {'status': 'poll editing successful'}
        return Response(context)