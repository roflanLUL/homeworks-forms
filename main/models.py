from django.contrib.auth.models import User
from django.db import models


class StrHistory(models.Model):
    date = models.CharField(max_length=10)
    time = models.CharField(max_length=8)
    istring = models.CharField(max_length=200)
    word_cnt = models.IntegerField()
    nmbr_cnt = models.IntegerField()
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
