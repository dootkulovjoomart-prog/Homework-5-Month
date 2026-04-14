from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User 
from .serializers import RegisterSerialiser
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
import random
from .models import UserConfirm


@api_view(['POST'])
def registration_api_views(request):
    serializer = RegisterSerialiser(data= request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')


    user = User.objects.create_user(
        username = username , 
        password = password , 
        is_active = False
    )

    code = str(random.randint(100000 , 999999))
    UserConfirm.objects.create(
        user = user,
        code = code 
    )
    
    print('Code add' , code)

    return Response(
        status=status.HTTP_201_CREATED,
        data={'user_id' : user.id }
    )   


@api_view(['POST'])
def authorization_api_views(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(
        username = username ,
        password = password
    )

    if user is not None :
        try:
            token = Token.objects.get( user = user )
        except:
            token = Token.objects.create( user = user )   
        return Response(data = {'key' : token.key})
    return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(["POST"])
def confirm_api_views(request):
    username = request.data.get('username')
    code = request.data.get('code')
    
    try:
        user = User.objects.get( username=username )
        confirm = UserConfirm.objects.get( user = user )
        if confirm.code == code :
            user.is_active = True
            user.save()
            confirm.delete()

            return Response('User add')
        else:
            return Response({'error'} , status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response({'error not Found user'} , status=status.HTTP_401_UNAUTHORIZED)
        
