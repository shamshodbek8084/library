from django.shortcuts import render
from .serializer import Book_Serializer, Rating_Serializer, ImageBook_Serializer
from .permissions import IsAdmin, IsUser
from .models import Category, Book, Rating_Book, Image_Book
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.filters import SearchFilter

# Create your views here.
# --------------------------------------------------------CRUD_BOOK--------------------------------------------

class CreateBook_View(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = Book_Serializer
    permission_classes = [IsAdmin]

class ListBook_View(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = Book_Serializer
    permission_classes = [IsAdmin]

class ReadBook_View(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = Book_Serializer

class DeleteBook_View(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = Book_Serializer
    permission_classes = [IsAdmin, ]

    def delete(self, request, *args, **kwargs):
        book = self.get_object()
        name = book.name
        book.delete()
        data = {
            "status" : True,
            "msg" : f"{name} nomli kitob o'chirildi"
        }

        return Response(data=data)
    
# --------------------------------------------------------RATING--------------------------------------------

class Create_Rating(CreateAPIView):
    queryset = Rating_Book.objects.all()
    serializer_class = Rating_Serializer
    permission_classes = [IsUser, ]
    
class Change_Rating(UpdateAPIView):
    queryset = Rating_Book.objects.all()
    serializer_class = Rating_Serializer
    permission_classes = [IsUser, ]
    
class All_Rating(ListAPIView):
    queryset = Rating_Book.objects.all()
    serializer_class = Rating_Serializer
    permission_classes = [IsAdmin, ]

class Decrease_Rating(ListAPIView):
    queryset = Rating_Book.objects.all().order_by('-rating')
    serializer_class = Rating_Serializer
    permission_classes = [IsAuthenticated]

# --------------------------------------------------------Image_Book--------------------------------------------

# class Image_Book(CreateAPIView):
#     queryset = Image_Book.objects.all()
#     serializer_class = ImageBook_Serializer
#     permission_classes = [IsAdmin]

# class List_Image_Book(ListAPIView):
#     queryset = Image_Book.objects.all()
#     serializer_class = ImageBook_Serializer
#     permission_classes = [IsAdmin]

# --------------------------------------------------------Search_Book--------------------------------------------

class Search_Book_View(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = Book_Serializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['author', 'name']

# --------------------------------------------------------Wishlist_Book--------------------------------------------
