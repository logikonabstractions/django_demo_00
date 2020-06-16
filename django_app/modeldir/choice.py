from django.db import models
from .question import Question

class Choice(models.Model):
    question            = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text         = models.CharField(max_length=200, default='option 1')
    votes               = models.IntegerField(default=0)