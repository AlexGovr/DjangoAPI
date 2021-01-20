from datetime import datetime
from django.db import models


class Question(models.Model):
    text = models.CharField(default='', null=True, max_length=240)
    #choices
    _TEXT = 'text'
    _ONE = 'choose_one'
    _MANY = 'choose_many'
    TYPE_CHOICES = [(_TEXT, 'text'), (_ONE, 'choose one answer'), (_MANY, 'choose one or more answers')]
    type = models.CharField(choices=TYPE_CHOICES, blank=True, default=_TEXT, max_length=20)


class Poll(models.Model):
    name = models.CharField(default='NoName', null=True, max_length=80)
    date_start = models.DateTimeField(default=datetime.now, blank=True, editable=False)
    date_end = models.DateTimeField(blank=True)
    description = models.CharField(default='', null=True, max_length=80)
    questions = models.ManyToManyField(Question, blank=True)


class FinishedPoll(models.Model):
    poll_id = models.ForeignKey(Poll, blank=True, on_delete='cascade')
    user_id = models.IntegerField(blank=True)


class Answer(models.Model):
    question = models.ForeignKey(Question, blank=True, on_delete='cascade')
    finished_poll = models.ForeignKey(FinishedPoll, blank=True, on_delete='cascade', null=True)
    text = models.CharField(default='', null=True, max_length=360)