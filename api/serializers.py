from rest_framework import serializers
from .models import (
    Usersignup,
    Trainersignup, 
    Usersession, 
    Trainersession,
    Promocode
)
from django.contrib.auth import get_user_model
from rest_framework.response import Response

User = get_user_model()

#Trainer
class TrainerSignUpSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Trainersignup
        fields = '__all__' 

class TrainerDetails(serializers.ModelSerializer):
     class Meta:
        model = Trainersignup
        exclude = ['password','device_token','device_type', 'latitude','longitude']


class TrainerSessionSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Trainersession
        fields = '__all__'

class FavroitesTrainerSessionSerilizer(serializers.ModelSerializer):
     class Meta:
        model = Trainersignup
        exclude = ['password','device_token','device_type', 'access_token','latitude','longitude'] 

class SignUpSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Usersignup
        fields = '__all__'
        
class UpdateUserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Usersignup
        exclude = ['password']

class CreateUserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Usersignup
        fields = '__all__'

class Update_DeviceTokenUserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Usersignup
        fields = ('user_id','device_token','device_type')
        
class CreateSessionSerilizer(serializers.ModelSerializer):
    class Meta():
        model = Usersession
        fields = '__all__'

class PromocodeUse(serializers.ModelSerializer):
    class  Meta():
        model = Promocode
        fields = '__all__'
