from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Event(models.Model):
    name = models.TextField()
    description = models.TextField()
    date = models.DateTimeField()
    people = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


