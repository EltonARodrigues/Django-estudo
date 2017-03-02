from django.db import models


class Users(models.Model):
    user = CharField(max_length=30)
    password = models.CharField(max_length=50)
