from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Item,Shop
from rest_framework.generics import ListAPIView
from .serializer import *
from accounts.models import Player


class ListShop(ListAPIView):
    queryset = Shop.objects.all()
    serializer_class =ShopSerializer

class BuyItem(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id_item):
        p = Player.objects.get(user_id=request.user.id)
        if id_item == 5:
            p.limit += 3
            return Response("limit +3")
        item = Shop.objects.get(id=id_item)
        p = Player.objects.get(user_id=request.user.id)
        if p.points >= item.price:
            p.points = p.points - item.price
            p.save()
            Item.objects.create(user=p, item=item)
            return Response('Item was successfully',status=status.HTTP_200_OK)
        else:
            return Response("no many",status=status.HTTP_400_BAD_REQUEST)

