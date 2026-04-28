from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from .models import CustomUser , UserConfirm


class UserBaseSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class RegisterSerialiser(serializers.Serializer):
    phone_namber = serializers.CharField(max_length=9 ,required=False , allow_blank=True  , allow_null=True) 
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate_username(self , email ):
        try:
            User.objects.get(email = email)
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
        user_id = attrs.get('user_id')
        code = attrs.get('code')

        try: 
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            raise ValidationError('User not found')
        
        try:
            confirm = UserConfirm.objects.get(user=user)
        except UserConfirm.DoesNotExist:
            raise ValidationError('Confirm not found')

        print("DB CODE:", confirm.code)
        print("INPUT CODE:", code)

        if confirm.code != code:
            raise ValidationError('Invalid code')

        return attrs