from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from polls_app.models import Poll, Question, QuestionPoint, UserQuestion


class QuestionPointSerializer(ModelSerializer):

    class Meta:
        model = QuestionPoint
        fields = '__all__'


class QuestionSerializer(ModelSerializer):
    questions = QuestionPointSerializer(source='questionpoint_set', many=True, read_only=True)

    class Meta:
        model = Question
        fields = '__all__'


class PollSerializer(ModelSerializer):
    questions = QuestionSerializer(source='question_set', many=True, read_only=True)

    class Meta:
        model = Poll
        fields = ['id', 'start_date', 'end_date', 'name', 'description', 'questions']


class UserQuestionSerializer(Serializer):
    questionpoints = QuestionPointSerializer(source='question_point', many=True)
    #
    user_id = serializers.IntegerField()
    question_id = serializers.IntegerField()
    text_answer = serializers.CharField(max_length=255, required=False, default='')

    def get(self):
        return UserQuestion.objects.all()

    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.question_id = validated_data.get('question_id', instance.question_id)
        instance.text_answer = validated_data.get('text_answer', instance.text_answer)
        return instance

    def validate(self, data):
        """
        Check that start is before finish.
        """
        if UserQuestion.objects.filter(question_id=data['question_id']).exists():
            raise serializers.ValidationError("You have already answered this question")
        return data

    def validate_questionpoints(self, value):
        type = Question.objects.get(pk=self.initial_data['question_id']).type
        if type == 'one_of':
            if len(value) != 1:
                raise serializers.ValidationError("Must be one point")

        if type == 'many_of':
            if len(value) < 1:
                raise serializers.ValidationError("Must be at least one point")
        return value

    def validate_text_answer(self, value):
        type = Question.objects.get(pk=self.initial_data['question_id']).type
        if type == 'text':
            if len(value) < 1:
                raise serializers.ValidationError("This field is required")
        return value


    # class Meta:
    #     model = UserQuestion
    #     fields = ['user_id', 'question_id', 'text_answer', 'questionpoints']
    #     depth = 3

    def create(self, validated_data):
        questionpoints_data = validated_data.pop('question_point')
        user_question = UserQuestion.objects.create(**validated_data)
        for questionpoint in questionpoints_data:
            user_question.question_point.create(**questionpoint)
        return user_question