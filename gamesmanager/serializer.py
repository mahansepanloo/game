from rest_framework import serializers
from .models import Bottle
from accounts.models import Player
class SerializerSend(serializers.ModelSerializer):
    class Meta:
        model = Bottle
        fields = ["id","text","answer"]





class SerializerList(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    class Meta:
        model = Player
        fields = ['username',"rank"]


