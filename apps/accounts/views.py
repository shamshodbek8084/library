from django.shortcuts import render
from rest_framework.generics import CreateAPIView, GenericAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializer import Register_Serializer, Login_Serializer
from django.contrib.auth.models import User
from rest_framework.response import Response

# Create your views here.

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Register_Serializer
    permission_classes = [AllowAny, ]

class LoginView(GenericAPIView):
    serializer_class = Login_Serializer
    permission_classes = [AllowAny, ]
    def post(self, request):
        serializer = self.get_serializer(data = request.data)

        if serializer.is_valid():
            data = {
            "status" : True,
            "msg" : "Login is Succesfully",
            "access": serializer.validated_data['access'],
            "refresh": serializer.validated_data['refresh']
            }
            return Response(data)
        
        data1 = {
            "status" : True,
            "msg" : "Login is not Succesfully",
        }
        return Response(data1)
    
class LogoutView(DestroyAPIView):
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        return self.request.user
    
    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        username = user.username
        user.delete()
        data = {
            "status" : True,
            "msg" : f"{username} nomli foydalanuvchi o'chirildi"
        }

        return Response(data=data)
    
