from rest_framework import serializers  
from .models import Category , Product , Review 
from rest_framework.exceptions import ValidationError

 
class CategoryListSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = 'id name  products '.split()

    def get_products(self,obj):
        return obj.products.count()
class ProductListSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta :
        model = Product
        fields = '__all__'
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


class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required = True)


class ProductValidateSerializers(serializers.Serializer):
    title = serializers.CharField(required = True    )
    description = serializers.CharField(required = False)
    price = serializers.IntegerField()
    category_id = serializers.IntegerField()

    def validate_category_id(self , category_id):
        try:
            Category.objects.get(id =category_id)
        except Category.DoesNotExist:
            raise ValidationError('Category does not exixt')
        return category_id
    
class ReviewsValidateSErializers(serializers.Serializer):
        text = serializers.CharField(required = True)
        stars = serializers.IntegerField(max_value = 5 , min_value = 1)
        product_id = serializers.IntegerField()

        def validate_product_id(self , product_id):
            try:
                Review.objects.get(id = product_id)
            except Review.DoesNotExist:
                raise ValidationError('Product does not exixt ')
            return product_id
        

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('owner',)