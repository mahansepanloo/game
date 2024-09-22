import random
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Bottle
from .serializer import *
from .models import Player
from shop.models import Item
from shop.serializer import SerializerItem


def distance(x1: int, x2: int, y1: int, y2: int) -> float:
    """
    Calculate the Euclidean distance between two points in a 2D space.

    Args:
        x1 (int): x-coordinate of the first point.
        x2 (int): x-coordinate of the second point.
        y1 (int): y-coordinate of the first point.
        y2 (int): y-coordinate of the second point.

    Returns:
        float: The calculated distance between the two points.
    """
    z = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)
    return z


class SentLetterView(APIView):
    """
    API view for sending letters (in bottles).

    This view handles the process of sending letters by creating a new
    Bottle instance if the player has sufficient characters left and
    decrements their limit.

    Permission:
        Requires the user to be authenticated.

    Methods:
        post(request):
            Handles POST requests to send a letter in a bottle.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Handle sending a letter in a bottle.

        Args:
            request: The HTTP request object containing the necessary data.

        Returns:
            Response: A response indicating success or failure of sending the letter,
                      with the appropriate status code.
        """
        data = request.data
        player = Player.objects.get(user=request.user)
        try:
            item = Item.objects.get(user=player, item_id=int(data['item_id']))
        except Item.DoesNotExist:
            return Response("Item does not exist", status=status.HTTP_404_NOT_FOUND)

        if item.item.characters < len(data['text']):
            return Response({f"You can't add more than {item.item.characters} characters"},
                            status=status.HTTP_400_BAD_REQUEST)

        player.limit -= 1
        player.save()

        Bottle.objects.create(
            sender=player,
            max_x=player.x + item.item.km,
            min_x=player.x - item.item.km,
            max_y=player.y + item.item.km,
            min_y=player.y - item.item.km,
            text=data['text']
        )
        item.delete()
        return Response({"message": "create"}, status=status.HTTP_201_CREATED)


class GetLetterView(APIView):
    """
    API view for receiving letters (from bottles).

    This view allows authenticated users to receive letters from available bottles
    within their coordinates if they have not exceeded their daily limit.

    Methods:
        get(request):
            Handles GET requests to retrieve a letter from a bottle.
    """

    def get(self, request):
        """
        Handle receiving a letter from a bottle.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A response indicating success or failure of receiving the letter,
                      with the appropriate status code.
        """
        player1 = Player.objects.get(user=self.request.user)
        if player1.limit <= 0:
            return Response(f"You can't add more 3 send in a day")

        bottles = Bottle.objects.filter(
            max_x__gte=player1.x,
            min_x__lte=player1.x,
            max_y__gte=player1.y,
            min_y__lte=player1.y,
            available=True
        ).exclude(sender__user=request.user)

        if not bottles.exists():
            return Response({"message": "No available bottles found."}, status=status.HTTP_404_NOT_FOUND)

        player1.points += 1000
        player1.rank += 1
        player1.save()

        chose = random.choice(bottles)
        chose.receiver = player1
        chose.available = False
        chose.save()

        return Response({"message": "Bottle received successfully.", "bottle_id": chose.id}, status=status.HTTP_200_OK)


class ListGetBottles(generics.ListAPIView):
    """
    API view for listing received bottles.

    This view allows authenticated users to view bottles they have received.

    Methods:
        get_queryset():
            Filter to return bottles received by the authenticated user.
    """
    queryset = Bottle.objects.all()
    serializer_class = SerializerSend
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return a queryset of bottles received by the authenticated user.

        Returns:
            QuerySet: Filtered bottles received by the user.
        """
        return Bottle.objects.filter(receiver__user=self.request.user)


class ListSendBottles(generics.ListAPIView):
    """
    API view for listing sent bottles.

    This view allows authenticated users to view bottles they have sent.

    Methods:
        get_queryset():
            Filter to return bottles sent by the authenticated user.
    """
    queryset = Bottle.objects.all()
    serializer_class = SerializerSend
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return a queryset of bottles sent by the authenticated user.

        Returns:
            QuerySet: Filtered bottles sent by the user.
        """
        return Bottle.objects.filter(sender__user=self.request.user)


class ListItem(generics.ListAPIView):
    """
    API view for listing items.

    This view allows authenticated users to view items they own.

    Methods:
        get_queryset():
            Filter to return items owned by the authenticated user.
    """
    queryset = Item.objects.all()
    serializer_class = SerializerItem
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return a queryset of items owned by the authenticated user.

        Returns:
            QuerySet: Filtered items owned by the user.
        """
        return Item.objects.filter(user__user=self.request.user)


class Answer(APIView):
    """
    API view for answering a received letter.

    This view allows authenticated users to provide an answer to a letter in a bottle.

    Permission:
        Requires the user to be authenticated.

    Methods:
        post(request):
            Handles POST requests to submit an answer.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Handle providing an answer to a letter.

        Args:
            request: The HTTP request object containing the answer data.

        Returns:
            Response: A response indicating success or failure of submitting the answer,
                      with the appropriate status code.
        """
        data = request.data
        if data["p"] == "4":
            try:
                permission = Item.objects.get(user__user=request.user, item__id=data['p'])
            except Item.DoesNotExist:
                return Response('you cannot answer', status=status.HTTP_400_BAD_REQUEST)

            b = Bottle.objects.get(id=data['b'], receiver__user=self.request.user)
            b.answer = data['a']
            b.save()
            permission.delete()
            return Response('answer success', status=status.HTTP_200_OK)

        return Response('you cannot answer', status=status.HTTP_400_BAD_REQUEST)


class Ranking(generics.ListAPIView):
    """
    API view for listing player rankings.

    This view provides a ranked list of players based on their rank.

    Methods:
        get_queryset():
            Returns all players sorted by rank in descending order.
    """
    queryset = Player.objects.all().order_by('-rank')
    serializer_class = SerializerList
    permission_classes = [IsAuthenticated]