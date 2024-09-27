from django.db import models
from accounts.models import Player


class Bottle(models.Model):
    sender = models.ForeignKey(Player, on_delete=models.CASCADE,related_name='sbottle',blank=True,null=True)
    receiver = models.ForeignKey(Player, on_delete=models.CASCADE,null=True, blank=True)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    max_x = models.FloatField()
    min_x = models.FloatField()
    max_y = models.FloatField()
    min_y = models.FloatField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.sender.user.username


class Answer(models.Model):
    user = models.ForeignKey(Player, on_delete=models.CASCADE,related_name='uA')
    question = models.ForeignKey(Bottle, on_delete=models.CASCADE,related_name='qA')
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return self.user.user.username


