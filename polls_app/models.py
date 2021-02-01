from django.db import models


# Create your models here.
class Poll(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Question(models.Model):
    TYPE_CHOICES = [
        ('text', 'Text'),
        ('one_of', 'One Of'),
        ('many_of', 'Many Of'),
    ]

    poll = models.ForeignKey(Poll, models.CASCADE)
    question = models.CharField(max_length=255)
    type = models.CharField(choices=TYPE_CHOICES, max_length=30)

    def __str__(self):
        return self.question


class QuestionPoint(models.Model):
    name = models.CharField(max_length=255)
    question = models.ForeignKey(Question, models.CASCADE)

    def __str__(self):
        return self.name


class UserQuestion(models.Model):
    user_id = models.IntegerField()
    question = models.ForeignKey(Question, models.CASCADE)
    text_answer = models.CharField(max_length=255, blank=True)
    question_point = models.ManyToManyField(QuestionPoint, blank=True)

    def __str__(self):
        return str(self.user_id) + ' ' + self.question.question


