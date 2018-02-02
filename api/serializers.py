from rest_framework import serializers
from .models import Signup
from django.contrib.auth import get_user_model
from rest_framework.response import Response

User = get_user_model()

class SignUpSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Signup

        fields = ('user_id','first_name','last_name','email_id','age','gender','level','access_token','password','device_token','device_type','image')


class UpdateUserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        fields = ('user_id','first_name', 'last_name', 'email_id', 'age', 'gender', 'level','image')

class UpdateUserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        fields = ('user_id','first_name', 'last_name', 'email_id', 'age', 'gender', 'level','image')

class CreateUserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        fields = ('user_id', 'first_name', 'last_name', 'email_id', 'age', 'gender', 'level','access_token','image')



class Update_DeviceTokenUserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        fields = ('user_id','device_token','device_type')

