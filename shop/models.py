from django.db import models
from accounts.models import Player

class Shop(models.Model):
    name = models.CharField(max_length=100)
    characters = models.PositiveIntegerField()
    km = models.PositiveIntegerField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    user = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.user.username


