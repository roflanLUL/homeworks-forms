from django.contrib.auth.models import User
from django.db import models


class StrHistory(models.Model):
    date = models.CharField(max_length=10)
    time = models.CharField(max_length=8)
    string = models.CharField(max_length=200)
    word_count = models.IntegerField(default=None)
    number_count = models.IntegerField(default=None)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
