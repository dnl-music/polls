from datetime import datetime

from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from polls_app.models import *
# Create your views here.
from polls_app.serializers import PollSerializer, QuestionSerializer, UserQuestionSerializer


# class PollViewSet(ModelViewSet):
#     serializer_class = PollSerializer
#     queryset = Poll.objects.all()


class PollViewSet(ViewSet):

    def list(self, request):
        queryset = Poll.objects.filter(end_date__gt=datetime.now().strftime("%Y-%m-%d"))
        serializer = PollSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Poll.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = PollSerializer(user)
        return Response(serializer.data)


class QuestionViewSet(ViewSet):

    def list(self, request):
        queryset = Question.objects.all()
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Question.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = QuestionSerializer(user)
        return Response(serializer.data)


class UserQuestionViewSet(ViewSet):

    def list(self, request):
        user_id = self.request.query_params.get('user_id', None)
        if not user_id:
            return Response(status=400, data={'error': 'Query parameter user_id is required'})
        queryset = UserQuestion.objects.filter(user_id=user_id)#select_related('question_point').all()
        serializer = UserQuestionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = UserQuestion.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserQuestionSerializer(user)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserQuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors)