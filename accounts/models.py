from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.FloatField(default=1500)
    x = models.FloatField()
    y = models.FloatField()
    limit = models.IntegerField(default=3)
    rank = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} x {self.x} y {self.y}"


