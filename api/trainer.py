from __future__ import unicode_literals
from django.core.mail import EmailMessage

import random
from rest_framework import generics
from .serializers import  (
    TrainerSignUpSerilizer, 
    TrainerSessionSerilizer,
    TrainerDetails
)
from .models import (
    Usersignup, 
    Trainersignup
)

from .utility import (
    validate_email, 
    check_Token, 
    validate_date, 
    trainersignup_validation, 
    usersignup_validation, 
    session_validation, 
    editprofile_validation,
    excuate_query
    )

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils.crypto import get_random_string
import base64
from pushjack import APNSSandboxClient
import os
from django.http import HttpResponse
from django.template import loader, Context
from django.shortcuts import render
from django.views.generic import TemplateView
import forms


# Signup Trainer
@api_view(['POST'])
def signup_trainer(request):
    if request.method == 'POST':
        print request.data['password']
        validate = trainersignup_validation(request)
        if validate != "":
            return Response({'msg':validate, 'status_code':status.HTTP_400_BAD_REQUEST, 'status':"fail"})

        unique_id = get_random_string(length=32)
        request.data['access_token'] = unique_id
        request.data['password'] = base64.b64encode(request.data['password'])
        request.data['trainer_code'] = "MYOS-" + str(random.randint(10000, 99999))
        trainer_serilizer = TrainerSignUpSerilizer(data = request.data)
        if trainer_serilizer.is_valid():
            trainer_serilizer.save()
            user = Trainersignup.objects.get(email_id=request.data['email_id'], password=request.data['password'])
            obj_serializer = TrainerDetails(user)
            return Response({'status': "success", 'users': obj_serializer.data, 'status_code':status.HTTP_201_CREATED})
        else:
            return Response({'msg':trainer_serilizer.errors,'status_code':status.HTTP_400_BAD_REQUEST,'status': "fail"})

# Log In            
@api_view(['POST'])
def trainer_login(request):
    if request.method == "POST":
        print request.data
        email = request.data['email_id']
        password = base64.b64encode(request.data['password'])
        try:
            user = Trainersignup.objects.get(email_id=email)
            if user:               
                user.access_token = get_random_string(length=32)
                user.device_token = request.data['device_token']
                user.device_type = request.data['device_type']
                user.save(update_fields=["access_token","device_type","device_token"])
                #base64.b64decode(user.password) 
                serializer = TrainerDetails(user)
                return Response({'status': "success", 'users': serializer.data, 'status_code': status.HTTP_200_OK})
            else:
                return Response({'msg':"Invalid credentials",'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"})

        except Exception as e:
            print e
            return Response({'msg': "This username/email is not valid",'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"})

# Logout User
@api_view(['POST'])
def user_logout(request):

    if request.method == 'POST':
        try:
           
            user = Trainersignup.objects.get(user_id=request.data['user_id'])
            print "first_name" +user.first_name

            token_str = check_Token(user, request)

            if token_str != "":
                return Response({'msg': token_str, 'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"})

        except Exception as e:
            return Response({'msg': e, 'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"})

        if request.method == "POST":
            if user:
                try:
                    user.access_token = ""
                    user.device_token = ""
                    user.device_type = ""
                    user.save(update_fields=["access_token","device_type","device_token"])
                    return Response({'status': "success", 'msg':"User logout successfully.", 'status_code': status.HTTP_200_OK})
                except Exception as e:
                    return Response({'msg': e, 'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"})
