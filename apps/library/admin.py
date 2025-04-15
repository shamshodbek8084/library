from django.contrib import admin
from .models import Category
# Register your models here.



class Category_admin(admin.ModelAdmin):
    list_display = ('id', 'name') 
    search_fields = ('name', )
    list_filter = ('name', )   

admin.site.register(Category, Category_admin)