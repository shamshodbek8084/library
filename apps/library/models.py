from django.db import models
from apps.base.models import BaseModel
from django.contrib.auth.models import User

# Create your models here.

class Category(BaseModel):
    name = models.CharField(max_length=256, verbose_name="title")

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Book(BaseModel):
    name = models.CharField(max_length=256, verbose_name='Kitob nomi')
    category = models.ForeignKey(Category, on_delete = models.RESTRICT, null=True)
    file = models.FileField(upload_to='file/',verbose_name ='File')
    description = models.TextField(verbose_name='Kitob haqida', null=True, blank=True)


    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.name
    
class Image_Book(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='book_images/')

    class Meta:
        verbose_name = 'Image_Book'
        verbose_name_plural = 'Image_Books'

    def __str__(self):
        return f"{self.image.name} uchun rasm"
    
    
class Rating_Book(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    SCORE = [
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
    ]
    rating = models.PositiveIntegerField(choices=SCORE, verbose_name='Rating')

    class Meta:
        unique_together = ('book', 'user')

    def __str__(self):
        return (f"{self.user.username} nomli foydalanuvchi, {self.book.name}"
                f"kitobiga 5 dan {self.rating} baho qo'ydi")

class Wishlist_Book(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Wishlist'
        verbose_name_plural = 'Wishlists'

    def __str__(self):
        return f"{self.user.username} - {self.books.name}"
    

class Orders_Book(BaseModel):
    books = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0, verbose_name='Kitoblar Soni')
    total_price = models.IntegerField(verbose_name='Jami Narxi')
    STATUS = [
        ('start', 'Buyurtma rasmiylashtirildi'),
        ('awarage', 'Buyurtma yigilyapti'),
        ('medium', 'Buyurtma yulda'),
        ('end', 'Buyurtma sizda'),
    ]
    status = models.CharField(max_length=256, choices=STATUS, verbose_name='Buyurtma Holati')

    class Meta:
        verbose_name = 'Orders_Book'
        verbose_name_plural = 'Orders_Books'
    
    def __str__(self):
        return f"{self.user.username} - {self.quantity} - {self.total_price} - {self.books.name}"


class Comment(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='book', related_name='book_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user', related_name='user_comment')
    text = models.TextField(verbose_name='comment')

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f'{self.user} - {self.book}'
    

