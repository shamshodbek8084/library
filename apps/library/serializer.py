from rest_framework.serializers import ModelSerializer
from .models import Category, Book, Rating_Book, Image_Book, Wishlist_Book
from .permissions import IsAdmin, IsUser

class Book_Serializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class Rating_Serializer(ModelSerializer):
    class Meta:
        model = Rating_Book
        fields = '__all__'

class ImageBook_Serializer(ModelSerializer):
    class Meta:
        model = Image_Book
        fields = '__all__'

class Wishlist_Book(ModelSerializer):
    class Meta:
        model = Wishlist_Book
        fields = '__all__'