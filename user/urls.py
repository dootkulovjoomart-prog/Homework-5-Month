from django.urls import path
from .views import *


urlpatterns = [
    path('api/v1/registration/', RegisterApiView.as_view()) , 
    path('api/v1/authorization/' , AuthorizatiionAPIView.as_view()) , 
    path('api/v1/confirm/' , ConfirmAPIView.as_view())

]