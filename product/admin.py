from django.contrib import admin
from .models import Category , Product , Review
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id"]
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["id"]
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id" , "title"]


