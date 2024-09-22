from rest_framework import serializers
from .models import *



class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class SerializerItem(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
