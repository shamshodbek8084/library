from django.shortcuts import render
from .serializer import Book_Serializer
from .permissions import IsAdmin, IsUser
from .models import Category, Book
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView

# Create your views here.

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