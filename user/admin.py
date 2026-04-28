from django.contrib import admin
from .models import UserConfirm , CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(UserConfirm)
class UserConfirmAdmin(admin.ModelAdmin):
    list_display = ['id', 'user' , 'code' ]


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['id','email','is_active','is_staff']

    list_filter = ('is_staff', 'is_active')
    
    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        ('Права доступа', {
            'fields': ('is_staff', 'is_active', 'is_superuser')
        }),
    )

    ordering = ('email',)