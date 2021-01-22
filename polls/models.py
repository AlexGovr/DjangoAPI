from datetime import datetime
from django.db import models


class Question(models.Model):
    text = models.CharField(default='', null=True, max_length=240)
    #choices
    _TEXT = 'text'
    _ONE = 'choose_one'
    _MANY = 'choose_many'
    TYPE_CHOICES = [(_TEXT, 'text'), (_ONE, 'choose one answer'), (_MANY, 'choose one or more answers')]
    question_type = models.CharField(choices=TYPE_CHOICES, blank=True, default=_TEXT, max_length=20)

    def __str__(self):
        return f'{self.question_type}: {self.text}'


class Poll(models.Model):
    name = models.CharField(default='NoName', null=True, max_length=80)
    date_start = models.DateTimeField(default=datetime.now, blank=True, editable=False)
    date_end = models.DateTimeField(blank=True)
    description = models.CharField(default='', null=True, max_length=80)
    questions = models.ManyToManyField(Question, blank=True)

    def __str__(self):
        return f'{self.name}: {self.date_start} -- {self.date_end}'


class FinishedPoll(models.Model):
    poll = models.ForeignKey(Poll, blank=True, on_delete=models.CASCADE)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return f'user_id: {self.user_id}, poll_id: {self.poll.id}'


class Answer(models.Model):
    question = models.ForeignKey(Question, blank=True, on_delete=models.CASCADE)
    finished_poll = models.ForeignKey(FinishedPoll, blank=True, on_delete=models.CASCADE)
    text = models.CharField(default='', null=True, max_length=360)

    def __str__(self):
        return f'q_id: {self.question.id}, finidhed_poll_id: {self.finished_poll.id}, text: {self.text}'