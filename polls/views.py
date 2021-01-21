
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Poll, Question
from .serializers import PollSerializer, QuestionSerializer


class BasicViewSet(viewsets.ModelViewSet):

    def destroy(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.not_auth_response()
        try:
            super().destroy(request, *args, **kwargs)
            # override default response as it raises ConnectionResetError: [WinError 10054]
            return Response({'status': 'successfuly deleted'})
        except Exception as e:
            print(e)
            return Response({'error': str(e)})
    
    def create(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.not_auth_response()
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            print(e)
            return Response({'error': str(e)})

    def not_auth_response(self):
        return Response({'status': 'rejected: not authenticated'})

    def get_instance(self, id_):
        return self.queryset(id=id_)

class PollViewSet(BasicViewSet):
    queryset = Poll.objects.all().order_by('-date_start', ).reverse()
    serializer_class = PollSerializer


class QuestionViewSet(BasicViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer