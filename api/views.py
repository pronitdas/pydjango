# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.mail import EmailMessage

import random
from rest_framework import generics
from .serializers import (
    SignUpSerilizer,
    CreateUserSerilizer,
    UpdateUserSerilizer, 
    CreateSessionSerilizer,  
    TrainerSessionSerilizer,
    FavroitesTrainerSessionSerilizer,
    PromocodeUse
    )
from .models import (
    Usersignup, 
    Trainersignup,
    Promocode
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
from datetime import datetime,timedelta
from pytz import timezone
# SignUp User
@api_view(['POST'])
def signup_user(request):
    print  request.data
    if request.method == 'POST':
        
        validateString = usersignup_validation(request)
        if validateString != "":
            return Response({'msg':validateString, 'status_code':status.HTTP_400_BAD_REQUEST, 'status':"fail"})
        
        unique_id = get_random_string(length=32)
        request.data['access_token'] = unique_id
        request.data['password'] = base64.b64encode(request.data['password'])
        
        signup_serializer = SignUpSerilizer(data = request.data)
        if signup_serializer.is_valid():
            signup_serializer.save()
            user = Usersignup.objects.get(email_id=request.data['email_id'], password=request.data['password'])
            obj_serializer = UpdateUserSerilizer(user)
            return Response({'status': "success", 'users': obj_serializer.data, 'status_code':status.HTTP_201_CREATED})
        else:
            return Response({'msg':signup_serializer.errors,'status_code':status.HTTP_400_BAD_REQUEST,'status': "fail"})



#Get User profile
@api_view(['POST'])
def user_profile(request):
    if request.method == 'POST':
        try:
            user = Usersignup.objects.get(user_id=request.data['user_id'])
            token_str = check_Token(user,request)
            if token_str != "":
                return Response({'msg':token_str,'status_code':status.HTTP_400_BAD_REQUEST,'status': "fail"})
            serializer = CreateUserSerilizer(user)
            users = excuate_query(request)
            return Response({'status': "success", 'users': serializer.data, 'status_code':status.HTTP_200_OK})
        except Exception as e:
            print(e)
            print "Invalid data"
            return Response({'msg':e ,'status_code':status.HTTP_400_BAD_REQUEST,'status': "fail"})
        

# Edit Profile
@api_view(['POST'])
def user_editprofile(request):
    if request.method == 'POST':
        try:
            user = Usersignup.objects.get(user_id=request.data['user_id'])
            validate = editprofile_validation(request, user)
            if validate != "":
                return Response({'msg':validate,'status_code':status.HTTP_400_BAD_REQUEST,'status': "fail"})
            serializer = UpdateUserSerilizer(user,data=request.data)
            if serializer.is_valid():
                if len(request.FILES) != 0:
                    user.image.delete()
                serializer.save()
                return Response({'status': "success", 'users': serializer.data, 'status_code':status.HTTP_200_OK})
            else:
                print serializer.errors
                return Response({'msg':serializer.errors,'status_code':status.HTTP_400_BAD_REQUEST,'status': "fail"})
            
        except Exception as e:
            print(e)
            print "Invalid data"
            return Response({'msg':e ,'status_code':status.HTTP_400_BAD_REQUEST,'status': "fail"})
         

# User Update, Get, Delete
@api_view(['GET', 'PUT', 'DELETE'])
def user_details(request,pk):
    print request.data
    try:
        user = Usersignup.objects.get(pk=pk)
        token_str = check_Token(user,request)
        if token_str != "":
            return Response({'msg':token_str,'status_code':status.HTTP_400_BAD_REQUEST,'status': "fail"})
    except Exception as e:
        print(e)
        print "Invalid data"
        return Response({'msg':"Invalid data" ,'status_code':status.HTTP_400_BAD_REQUEST,'status': "fail"})

    if request.method == 'GET':

        serializer = CreateUserSerilizer(user)
        return Response({'status': "success", 'users': serializer.data, 'status_code':status.HTTP_200_OK})

    elif request.method == 'PUT':

        validate_str = validate_email(request.data,pk)
        if validate_str != "":
            return Response({'msg': validate_str, 'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"})
        serializer = UpdateUserSerilizer(user,data=request.data)
        if serializer.is_valid():
            if len(request.FILES) != 0:
                user.image.delete()
            serializer.save()
            return Response({'status': "success", 'users': serializer.data, 'status_code':status.HTTP_200_OK})
        else:
            print serializer.errors
            return Response({'msg':serializer.errors,'status_code':status.HTTP_400_BAD_REQUEST,'status': "fail"})

    elif request.method == 'DELETE':
        user.image.delete()
        user.delete()
        return Response({'status': "success", 'msg': "Record Deleted Successfully", 'status_code':status.HTTP_200_OK})


# User Login
@api_view(['GET','POST'])
def user_login(request):
    if request.method == "POST":
        print request.data
        email = request.data['email_id']
        password = base64.b64encode(request.data['password'])

        try:
            user = Usersignup.objects.get(email_id=email,password=password)
            if user:               
                user.access_token = get_random_string(length=32)
                user.device_token = request.data['device_token']
                user.device_type = request.data['device_type']
                user.save(update_fields=["access_token","device_type","device_token"])

                serializer = CreateUserSerilizer(user)
                #if (user.device_type != "web"):
                 #   push_notification(user.device_token)
                return Response({'status': "success", 'users': serializer.data, 'status_code': status.HTTP_200_OK})
            else:
                return Response({'msg':"Invalid credentials",'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"})

        except Exception as e:
            print e
            return Response({'msg': "This username/email is not valid",'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"})

# Create Session
@api_view(['POST'])
def create_session(request):
    if request.method == "POST":
        print request
        
        validate = session_validation(request)
        if validate != "":
            return Response({'msg':validate,'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"})

        if request.data['session_type'] == "book_for_a_friend":
            request.data['squad_size'] == ""

        if request.data['session_type'] == "squad_session":
            request.data['first_name'] == ""
            request.data['last_name'] == ""
            request.data['gender'] == ""
            request.data['level'] == ""
        
        request.data['session_status'] = "created"
        request.data['session_id'] = get_random_string(length=10)
        create_serilizer = CreateSessionSerilizer(data= request.data)
        if create_serilizer.is_valid():
            
            create_serilizer.save()
            request.data['session_created_user_id'] = request.data['user_id']
            # Favorites Trainer is there
            if request.data['favorites_trainercode'] != "": 
                try:
                    user = Trainersignup.objects.get(trainer_code = request.data['favorites_trainercode'])
                    request.data['trainer_id'] = user.user_id

                except Exception as e:
                    print e
                
                trainer_Serilizer = TrainerSessionSerilizer(data = request.data)
                if trainer_Serilizer.is_valid():
                    trainer_Serilizer.save()
                else:
                    return Response({'msg':trainer_Serilizer.errors,'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"})
            else:
                print "pankaj"
                # excuate the query for fetch near by trainer
                rows = excuate_query(request)
                for i in rows:
                    try:
                        request.data['trainer_id'] = i[0]
                        trainer_Serilizer = TrainerSessionSerilizer(data = request.data)
                        if trainer_Serilizer.is_valid():
                            trainer_Serilizer.save()
                        else:
                            return Response({'msg':trainer_Serilizer.errors,'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"})
                    except Exception as e:
                        print e
                        return Response({'msg':e,'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"})
            return Response({'status': "success", 'users': create_serilizer.data, 'status_code': status.HTTP_200_OK})
        else:
            return Response({'msg':create_serilizer.errors,'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"})
        
        
# Logout User
@api_view(['POST'])
def user_logout(request):

    if request.method == 'POST':
        try:
           
            user = Usersignup.objects.get(user_id=request.data['user_id'])
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

# Update Device Token
@api_view(['POST'])
def update_deviceToken(request):
    if request.method == 'POST':
        try:
            user = Usersignup.objects.get(user_id=request.data['user_id'])
            token_str = check_Token(user, request)

            if token_str != "":
                return Response({'msg': token_str, 'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"})

        except Exception as e:
            return Response({'msg': e, 'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"})

        if request.method == "POST":
            if user:

                try:
                    user.device_token = request.data['device_token']
                    user.device_type = request.data['device_type']
                    user.save(update_fields=["device_type","device_token"])
                    return Response({'status': "success", 'msg':"Device Token updated successfully.", 'status_code': status.HTTP_200_OK})
                except Exception as e:
                    return Response({'msg': e, 'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"})



#Favroites Trainer
@api_view(['POST'])
def favroites_trainer(request):
    if request.method == 'POST':
        try:
            user = Usersignup.objects.get(user_id=request.data['user_id'])
            token_str = check_Token(user, request)

            if token_str != "":
                return Response({'msg': token_str, 'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"})

            users = Trainersignup.objects.all()
            favserilizer = FavroitesTrainerSessionSerilizer(users,many=True)
            return Response({'status': "success", 'users':favserilizer.data, 'status_code': status.HTTP_200_OK})
        except Exception as e:
            return Response({'msg': e, 'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"})


def push_notification(apns_token):

    url = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/orlink.pem'
    client = APNSSandboxClient(certificate=url,
                        default_error_timeout=10,
                        default_expiration_offset=2592000,
                        default_batch_size=100,
                        default_retries=5)
    alert = 'Hello world.'
    try:
        res = client.send(apns_token,
                      alert,
                      badge=10,
                      sound='default',
                      extra={'custom': 'data'})
        print res.tokens
    except:
        print(res.token_errors)
    client.close()

@api_view(['POST'])
def apply_promocode(request):
    if request.method == 'POST':

        try:
           
            user = Usersignup.objects.get(user_id=request.data['user_id'])

            token_str = check_Token(user, request)

            if token_str != "":
                return Response({'msg': token_str, 'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"})
            obj = Promocode.objects.get(promo_code=request.data['promo_code'])

            if obj:
                import dateutil.parser

                #now = datetime.now()
                
                date_time1 ='2018-03-29 23:00:59+00:00'
                now = dateutil.parser.parse(date_time1)

                datetime_obj_utc = now.replace(tzinfo=timezone('UTC'))
                current_date = datetime_obj_utc.strftime("%Y-%m-%d %H:%M:%S+00:00")
                print obj.expiry_date
                diff = now-obj.expiry_date
                days = diff.days
                if days <= 0:

                    print (str(days) + ' day(s)')
                    days_to_hours = days * 24
                    diff_btw_two_times = (diff.seconds) / 3600
                    overall_hours = days_to_hours + diff_btw_two_times
                    print (str(overall_hours) + ' hours')
                    hours = (diff.seconds) / 3600  
                    print (str(hours) + ' Hours')
                    #same for minutes just divide the seconds by 60
 
                    minutes = (diff.seconds) / 60
                    print (str(minutes) + ' Minutes')
                
                    #to print seconds, you know already ;)
                
                    print (str(diff.seconds) + ' secs')
 
                
                
                expiry_date = obj.expiry_date
                print current_date
                if expiry_date < current_date:
                    return Response({'msg':expiry_date,'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"})  
                else:
                    return Response({'msg':"promo code expired",'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"})  
            else:
                return Response({'msg':"Invalid promo code123",'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"})  

        except Exception as e:
            return Response({'msg': "Invalid promo code", 'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"})

         
        
