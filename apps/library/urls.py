from django.urls import path
from .views import (CreateBook_View,
                    ListBook_View,
                    ReadBook_View,
                    DeleteBook_View,
                    Create_Rating,
                    Change_Rating,
                    All_Rating,)


urlpatterns = [
    path('create_book/', CreateBook_View.as_view(), name='create_book'),
    path('list_book/', ListBook_View.as_view(), name='list_book'),
    path('read_one_view/<int:pk>/', ReadBook_View.as_view(), name='read_one_view'),
    path('delete_one_book/<int:pk>/', DeleteBook_View.as_view(), name='delete_one_book'),
    path('create_rating/', Create_Rating.as_view(), name='create_rating'),
    path('update_rating/<int:pk>/', Change_Rating.as_view(), name='update_rating'),
    path('list_rating/', All_Rating.as_view(), name='list_rating'),

]