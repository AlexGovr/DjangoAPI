from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from polls.views import PollViewSet, PollEditViewSet, QuestionViewSet

router = routers.DefaultRouter()
router.register(r'polls', PollViewSet)
router.register(r'polls_edit', PollEditViewSet)
router.register(r'questions', QuestionViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]