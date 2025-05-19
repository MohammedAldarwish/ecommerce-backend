from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser

class UserRegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration:
    - Validates that password and password confirmation match.
    - Creates a new user using the CustomUser model.
    - Hides the password fields from being returned in responses.
    """

    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'password', 'password_confirm')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError('Passwords do not match')
        return attrs
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

class UserLoginSerializer(serializers.Serializer):
    """
    Serializer for user login:
    - Accepts email and password for authentication.
    - Uses Django's `authenticate` to validate credentials.
    - Returns the user instance if authentication is successful.
    """

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials") 