from rest_framework import serializers 
from .models import Category , Product , Review 
 
class CategoryListSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = 'id name  products '.split()

    def get_products(self,obj):
        return obj.products.count()
class ProductListSerializer(serializers.ModelSerializer):
    class Meta :
        model = Product
        fields = 'id title description price category reviews category_list rating'.split()
        # depth = 1
    def get_rating(self , product ):
        return product.rating()
    
class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text product stars'.split()


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'