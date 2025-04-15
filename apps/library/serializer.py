from rest_framework.serializers import ModelSerializer
from .models import Category, Book
from .permissions import IsAdmin, IsUser

class Book_Serializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

