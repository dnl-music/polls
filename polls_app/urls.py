from django.contrib import admin
from django.urls import path, include
from polls_app.views import PollViewSet, QuestionViewSet, UserQuestionViewSet

urlpatterns = [
    path('polls', PollViewSet.as_view({'get': 'list'})),
    path('questions', QuestionViewSet.as_view({'get': 'list'})),
    path('user-questions', UserQuestionViewSet.as_view({'get': 'list', 'post': 'create'})),
]