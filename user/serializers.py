from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import CustomUser 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from . import utils


class OauthCodeSerializer(serializers.Serializer):
    code = serializers.CharField()

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['birthdate'] = str(user.birthdate)
        return token




class UserBaseSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class RegisterSerialiser(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15 ,required=False , allow_blank=True  , allow_null=True) 
    email = serializers.EmailField()
    password = serializers.CharField()
    birthdate = serializers.DateField()

    def validate_username(self , email ):
        try:
            CustomUser.objects.get(email = email)
        except:
            return email
        raise ValidationError('User already exists ! ')
    
class AuthValidateSerializer(UserBaseSerializer):
    pass

class ConfirmSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    code = serializers.CharField(max_length = 6)
    # def validate(self, attrs):
    #     user_id = attrs.get('user_id')
    #     code = attrs.get('code')
    #     try: 
    #         user = CustomUser.objects.get(id=user_id)
    #     except CustomUser.DoesNotExist:
    #         raise ValidationError('User None')
        
    #     try:
    #         UserConfirm.objects.get(user=user,code = code)
    #     except UserConfirm.DoesNotExist:
    #         raise ValidationError('Error')
    #     return attrs
    def validate(self, attrs):
        email = attrs.get('email')
        code = attrs.get('code')

        try: 
            user = CustomUser.objects.get(email = email)
        except CustomUser.DoesNotExist:
            raise ValidationError('User not found')
        if not utils.verifity_confirmation(email , code):
            raise serializers.ValidationError("error code  ")
        
        attrs['user'] = user
        return attrs
    def save(self , **kwargs):
        user = self.validated_data['user']
        user.is_active = True
        user.save()