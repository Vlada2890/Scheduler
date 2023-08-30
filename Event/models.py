from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Event(models.Model):
    name = models.TextField()
    description = models.TextField()
    date = models.DateTimeField()
    people = models.ForeignKey(User,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name






