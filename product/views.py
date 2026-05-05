from rest_framework.decorators import api_view 
from rest_framework.response import Response
from .models import Category , Product ,Review 
from .serialazers import *
from rest_framework import status
from django.db import transaction
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    GenericAPIView
)

from common.permissions import IsAuth , IsAnon , EditWithin15Minutes, IsModerator

from rest_framework.viewsets import ModelViewSet

from common.validators import validate_age_from_token

from rest_framework.mixins import (
    ListModelMixin , 
    CreateModelMixin ,
    DestroyModelMixin ,
    UpdateModelMixin ,
    RetrieveModelMixin
)



class CategoryListAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    pagination_class = PageNumberPagination
    

class CateforyDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'
    permission_classes = [IsAnon|IsModerator]

    def perform_create(self, serializer):
        validate_age_from_token(self.request)
        serializer.save(owner = self.request.user)
    

    def get_serializer_class(self):
        if self.request.method in ['GET' , 'POST']:
            return CreateProductSerializer
        return ProductListSerializer
    

class MixinAPIView(GenericAPIView,
                    ListModelMixin , 
                   CreateModelMixin , 
                   DestroyModelMixin , 
                   UpdateModelMixin ,
                   RetrieveModelMixin 
                   ):
    
    def get(self , request , *args , **kwargs ):
        return super().list(request , *args , **kwargs )
    
    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def delet(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    

class ReviewAPIView(MixinAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'
    
    


    






























































# @api_view(['GET', 'PUT' , 'DELETE'])

# def category_detail_api_view(request , id):
#     try:
#         category = Category.objects.get(id=id)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         data = CategoryDetailSerializer(category , many = False ).data
#         return Response(data= data)
#     elif request.method == 'DELETE':
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == 'PUT':
#         serializer = CategoryValidateSerializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         category.name = serializer.validated_data.get('name')
#         category.save()
#         return Response(status=status.HTTP_201_CREATED , 
#                         data= CategoryDetailSerializer(category).data)
        



# @api_view(['GET', 'PUT' , 'DELETE'])

# def product_detail_api_view(request , id):
#     try:
#         product = Product.objects.get(id=id)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         data = ProductDetailSerializer(product , many = False).data
#         return Response(data=data)
#     elif request.method == 'DELETE':
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif  request.method == 'PUT':
#         serializer = ProductValidateSerializers(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         product.title = serializer.validated_data.get('title')
#         product.description = serializer.validated_data.get('description')
#         product.price = serializer.validated_data.get('price')
#         product.category_id = serializer.validated_data.get('category_id')
#         product.save()
#         return Response(status=status.HTTP_201_CREATED , 
#                         data = ProductDetailSerializer(product).data)

# @api_view(['GET' ,'PUT' , 'DELETE'])

# def review_detail_api_view(request, id):
#     try:
#         review = Review.objects.get(id=id)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         data = ReviewDetailSerializer(review , many = False ).data
#         return Response(data=data)
#     elif request.method == 'DELETE':
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == 'PUT':
#         serializer = ReviewsValidateSErializers(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         review.text = serializer.validated_data.get('text')
#         review.stars = serializer.validated_data.get('stars')
#         review.product_id = serializer.validated_data.get('product_id')
#         review.save()
#         return Response(status=status.HTTP_201_CREATED, 
#                         data=ReviewDetailSerializer(review).data)

# @api_view(['GET' , 'POST'])

# def category_list_api_view(request):
#     if request.method == 'GET':
#         category = Category.objects.all()
#         data =  CategoryListSerializer(category , many = True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#          serializer = CategoryValidateSerializer(data = request.data)
#          if not serializer.is_valid():
#              return Response(status=status.HTTP_400_BAD_REQUEST , 
#                              data=serializer.errors)
#          name = serializer.validated_data.get('name')
#          print(request.data)

#          category = Category.objects.create(
#              name = name
#          )

#     return Response(status=status.HTTP_201_CREATED , 
#                     data = CategoryDetailSerializer(category).data)

# @api_view(['GET' , 'POST'])
# def product_list_api_view(request):
#     if request.method == 'GET':
#         product = Product.objects.select_related('category').all()
#         data = ProductListSerializer(product , many = True ).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializer = ProductValidateSerializers(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST , 
#                             data=serializer.errors)
        
#         title = serializer.validated_data.get('title')
#         description = serializer.validated_data.get('description')
#         price = serializer.validated_data.get('price')
#         category_id = serializer.validated_data.get('category_id')
#         print(request.data)

#         product = Product.objects.create(
#             title = title ,
#             description = description , 
#             price = price ,
#             category_id = category_id
#         )

#         return Response(status=status.HTTP_201_CREATED , 
#                         data = ProductDetailSerializer(product).data)
        

# @api_view(['GET' , 'POST'])

# def review_list_api_view(request):
#     if request.method == 'GET':
#         review = Review.objects.all()
#         data = ReviewListSerializer(review , many = True ).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializer = ReviewsValidateSErializers(data = request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST , 
#                             data=serializer.errors)
#         text = serializer.validated_data.get('text')
#         stars = serializer.validated_data.get('stars')
#         product_id = serializer.validated_data.get('product_id')
#         print(request.data)

#         review = Review.objects.create(
#             text = text,
#             stars = stars,
#             product_id = product_id
            
#         )

#         return Response(status=status.HTTP_201_CREATED , 
#                         data = ReviewDetailSerializer(review).data)

