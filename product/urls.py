from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/categories/', CategoryListAPIView.as_view()),
        path('api/v1/products/', ProductViewSet.as_view({
        'get' : 'list' , 'post' : 'create'
    })),
    path('api/v1/products/', ProductViewSet.as_view({
        'get' : 'retrive' , 'put' : 'update' , 'delete' : 'destroy'
    })),
    path('api/v1/reviews/', ReviewAPIView.as_view())

]
