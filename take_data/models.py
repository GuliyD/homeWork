from django.db import models


class UserData(models.Model):
    text1 = models.CharField(max_length=20)
    num1 = models.IntegerField()
    text2 = models.CharField(max_length=20)
    num2 = models.IntegerField()