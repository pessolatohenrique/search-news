from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=200, unique=True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name
