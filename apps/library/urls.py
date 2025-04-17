from django.urls import path
from .views import (CreateBook_View,
                    ListBook_View,
                    ReadBook_View,
                    DeleteBook_View,
                    Create_Rating,
                    Change_Rating,
                    All_Rating,
                    Decrease_Rating,
                    Search_Book_View,
                    Wishlist_Create,
                    ListWishlist_View,)


urlpatterns = [
    path('create_book/', CreateBook_View.as_view(), name='create_book'),
    path('list_book/', ListBook_View.as_view(), name='list_book'),
    path('read_one_view/<int:pk>/', ReadBook_View.as_view(), name='read_one_view'),
    path('delete_one_book/<int:pk>/', DeleteBook_View.as_view(), name='delete_one_book'),
    path('create_rating/', Create_Rating.as_view(), name='create_rating'),
    path('update_rating/<int:pk>/', Change_Rating.as_view(), name='update_rating'),
    path('list_rating/', All_Rating.as_view(), name='list_rating'),
    path('decrease_list_rating/', Decrease_Rating.as_view(), name='decrease_list_rating'),
    # path('create_image_book/', Image_Book.as_view(), name='create_image_book'),
    # path('list_image_book/', List_Image_Book.as_view(), name='list_image_book'),
    path('search_book/', Search_Book_View.as_view(), name='search_book'),
    path('wishlist_create/', Wishlist_Create.as_view(), name='wishlist_create'),
    path('list_wishlist_create/', ListWishlist_View.as_view(), name='list_wishlist_create'),

]