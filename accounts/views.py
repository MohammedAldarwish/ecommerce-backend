from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializers import UserRegisterSerializer, UserLoginSerializer

class RegisterView(APIView):
    """
    API endpoint for user registration:
    - Accepts user data and creates a new account.
    - Returns an authentication token and basic user info upon success.
    - Handles validation errors if the input is invalid.
    """

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user': {
                    'email': user.email,
                    'name': user.name
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    """
    API endpoint for user login:
    - Authenticates user credentials using the login serializer.
    - Returns an authentication token and basic user info if credentials are valid.
    - Responds with validation errors if authentication fails.
    """
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user': {
                    'email': user.email,
                    'name': user.name
                }
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)