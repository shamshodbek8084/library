from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    message = "Siz ushbu amalni bajarishingiz uchun Admin bo'lishingiz kerak"
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_superuser
    

class IsUser(BasePermission):
    message = "Siz ushbu amalni bajarishingiz uchun User bo'lishingiz kerak"
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and not request.user.is_superuser
    