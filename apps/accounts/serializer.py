from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Profile

class Profile_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['icon', 'phone_number', 'address', 'country', 'birth']


class Register_Serializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only = True)
    profile = Profile_Serializer(required = False)

    class Meta:
        model = User 
        fields = ['id', 'username', 'email', 'password', 'password2', 'profile']
        extra_kwargs = {
            'password' : {
                'write_only' : True
            }
        }

    def validate(self, data):
        if data['password'] != data['password2'] : 
            raise serializers.ValidationError('Parollar bir xil emas!')
        return data
    
    def create(self, validated_data):
        profile_data = validated_data.pop('profile', None)
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        if profile_data:
            Profile.objects.create(user=user, **profile_data)
        return user
    
class Login_Serializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ['username', 'password']
    
    def validate(self, data):
        username =  data.get("username")
        password =  data.get("password")
        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError("Username va Passwordni to'g'ri kiriting!")
        
        # Token yaratish
        tokens = RefreshToken.for_user(user)
        return {
            "refresh": str(tokens),
            "access": str(tokens.access_token)
        }