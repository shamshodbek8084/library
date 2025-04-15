from rest_framework.serializers import ModelSerializer
from .models import Category, Book, Rating_Book
from .permissions import IsAdmin, IsUser

class Book_Serializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class Rating_Serializer(ModelSerializer):
    class Meta:
        model = Rating_Book
        fields = '__all__'

