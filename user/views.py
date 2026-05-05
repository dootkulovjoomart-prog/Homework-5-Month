from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerialiser  ,AuthValidateSerializer , ConfirmSerializer , CustomTokenObtainPairSerializer
from rest_framework.generics import CreateAPIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
import random
from .models import UserConfirm , CustomUser
from rest_framework_simplejwt.views import TokenObtainPairView  


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class RegisterApiView(CreateAPIView):
    serializer_class = RegisterSerialiser
    def post(self , request):
        request.data.get("data")
        serializer = RegisterSerialiser(data= request.data)
        serializer.is_valid(raise_exception=True)

        phone_number = serializer.validated_data.get('phone_number')
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        birthdate = serializer.validated_data.get('birthdate')


        user = CustomUser.objects.create_user(
            email = email, 
            phone_number = phone_number ,
            password = password , 
            birthdate = birthdate , 
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


class AuthorizatiionAPIView(CreateAPIView):
    serializer_class = AuthValidateSerializer
    def post(self , request ):
        serializer = AuthValidateSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')

        user = authenticate(
            email = email,
            password = password
        )

        if user is not None :
            try:
                token = Token.objects.get( user = user )
            except:
                token = Token.objects.create( user = user )   
            return Response(data = {'key' : token.key})
        return Response(status=status.HTTP_401_UNAUTHORIZED)

class ConfirmAPIView(CreateAPIView):
    serializer_class = ConfirmSerializer
    def post(self , request):
        serializer=ConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_id = serializer.validated_data.get('user_id')
        code = serializer.validated_data.get('code')
        
        try:
            user = CustomUser.objects.get(id=user_id)
            confirm = UserConfirm.objects.get( user = user )
            if confirm.code == code :
                user.is_active = True
                user.save()
                confirm.delete()
                return Response('User add')
            else:
                return Response({'error'} , status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            return Response({'error not Found user'} , status=status.HTTP_401_UNAUTHORIZED)
        
            
   