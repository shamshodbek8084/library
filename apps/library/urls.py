from django.urls import path
from .views import (CreateBook_View,
                    ListBook_View,
                    ReadBook_View,
                    DeleteBook_View,)


urlpatterns = [
    path('create_book/', CreateBook_View.as_view(), name='create_book'),
    path('list_book/', ListBook_View.as_view(), name='list_book'),
    path('read_one_view/<int:pk>/', ReadBook_View.as_view(), name='read_one_view'),
    path('delete_one_book/<int:pk>/', DeleteBook_View.as_view(), name='delete_one_book'),

]