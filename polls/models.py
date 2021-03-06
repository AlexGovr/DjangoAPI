from datetime import datetime
from re import finditer
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
    finished_poll = models.ForeignKey(FinishedPoll, related_name='answers', blank=True, on_delete=models.CASCADE)
    text = models.CharField(default='', null=True, max_length=360)

    def save(self, *args, **kwargs):
        the_same_answer = Answer.objects.filter(question=self.question, finished_poll=self.finished_poll)
        if the_same_answer:
            raise Exception('there is already an answer with same question_id and finished_poll_id')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'question_id: {self.question.id}, finished_poll_id: {self.finished_poll.id}, text: {self.text}'