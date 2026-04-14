from django.urls import path
from .views import *


urlpatterns = [
    path('api/v1/registration/', registration_api_views) , 
    path('api/v1/authorization/' , authorization_api_views) , 
    path('api/v1/confirm/' , confirm_api_views)

]