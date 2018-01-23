from rest_framework import serializers
from .models import Signup
from django.contrib.auth import password_validation


class SignUpSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Signup

        fields = ('user_id','first_name','last_name','email_id','age','gender','level')




