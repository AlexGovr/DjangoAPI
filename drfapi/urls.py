from django.urls import include, path
from rest_framework import routers
from polls.views import PollViewSet, QuestionViewSet, FinishedPollViewSet, AnswerViewSet

router = routers.DefaultRouter()
router.register(r'poll', PollViewSet)
router.register(r'question', QuestionViewSet)
router.register(r'mypolls', FinishedPollViewSet)
router.register(r'answers', AnswerViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]