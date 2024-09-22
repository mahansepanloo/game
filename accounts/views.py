from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializer import *
from .models import *
from random import randint
from rest_framework.response import Response
from rest_framework import status

class RegisterView(APIView):
    """
    API view for user registration.

    This API view handles the registration of new users, creates a user account,
    and initializes a Player instance with random coordinates (x, y) in the game space.

    Methods:
        post(request):
            Handles POST requests for user registration.
    """

    def post(self, request):
        """
        Handle user registration via POST request.

        Args:
            request: The HTTP request object containing the user data.

        Returns:
            Response: A response indicating success or failure of registration,
                      with the appropriate status code.
        """
        serializer = Serializerregestar(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            while True:
                x = randint(1, 10)
                y = randint(1, 10)
                if not Player.objects.filter(x=x, y=y).exists():
                    break

            Player.objects.create(user=user, x=x, y=y)
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(TokenObtainPairView):
    """
    API view for user login.

    Inherits from `TokenObtainPairView` provided by the Django REST Framework.
    This view is responsible for handling user login and returning a JWT token pair
    (access token and refresh token).

    Methods:
        post(request):
            Handles POST requests for user authentication.
    """
    pass


class Refresh(TokenRefreshView):
    """
    API view for refreshing JWT tokens.

    Inherits from `TokenRefreshView` provided by the Django REST Framework.
    This view is responsible for handling requests to refresh the access token
    using a refresh token.

    Methods:
        post(request):
            Handles POST requests for refreshing the access token.
    """
    pass