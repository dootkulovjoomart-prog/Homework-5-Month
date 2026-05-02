from rest_framework.permissions import BasePermission , SAFE_METHODS
from datetime import timedelta
from django.utils import timezone

class IsAuth(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated #and not request.user.is_staff
    
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user    
    
class IsAnon(BasePermission):

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
    

class EditWithin15Minutes(BasePermission):
    def has_object_permission(self, request, view, obj):
        time_passsed = timezone.now() - obj.create_at
        return time_passsed <= timedelta(minutes=5)
    

class IsModerator(BasePermission):
    def has_permission(self, request, view): # type: ignore
        if request.user.is_superuser:
            return True
        if request.user.is_staff:
            if request.method == 'POST':
                return False
            return True
        
        return request.method in SAFE_METHODS
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or request.user.is_staff:
            return True
        
        return obj.director == request.user