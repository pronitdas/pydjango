# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from rest_framework import generics
from .serializers import SignUpSerilizer,CreateUserSerilizer,UpdateUserSerilizer
from .models import Signup
from rest_framework import status
import re
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from django.utils.crypto import get_random_string
import base64
from .utility import validate_email,check_Token
from push_notifications.models import APNSDevice

# Create your views here.

class SignUpUserView(generics.ListCreateAPIView):
    queryset = Signup.objects.all()
    serializer_class = SignUpSerilizer

    def perform_create(self, serializer):
        serializer.save()


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        isvalidate = self.validate(request.data)
        if isvalidate == False:
            return Response({'msg': "Password should be 8 to 15 charaters", 'status_code': 404,'status': "fail"}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():

            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({'status': "success", 'users': serializer.data, 'status_code':status.HTTP_201_CREATED}, status=status.HTTP_201_CREATED,
                            headers=headers)

        dict = {'msg':serializer.errors, 'status_code':status.HTTP_400_BAD_REQUEST,'status': "fail"}
        return Response(dict, status=status.HTTP_400_BAD_REQUEST)

    def validate(self,data):
        if data.get('password'):
            if  re.match(r'.{8,15}$', data.get('password')):
                return True
            else:

                return False

        return True

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Signup.objects.all()
    serializer_class = SignUpSerilizer

    def retrieve(self, request, *args, **kwargs):

        serializer = list(Signup.objects.all().values())
        if serializer:
            return Response({'status': "success", 'users': serializer, 'status_code': status.HTTP_201_CREATED},
                        status=status.HTTP_201_CREATED)
        dict = {'msg': serializer.errors, 'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"}
        return Response(dict, status=status.HTTP_400_BAD_REQUEST)


class GetRecord(generics.GenericAPIView):
    queryset = Signup.objects.all()
    serializer_class = SignUpSerilizer

    def post(self, request, *args, **kwargs):
        serializer = list(Signup.objects.filter(user_id=request.data['user_id']).values())
        if serializer:
            return Response({'status': "success", 'users': serializer, 'status_code': status.HTTP_201_CREATED},
                        status=status.HTTP_201_CREATED)
        return Response({'msg': serializer.errors, 'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"}, status=status.HTTP_400_BAD_REQUEST)

class UpdateRecord(generics.UpdateAPIView):
    queryset = Signup.objects.all()
    serializer_class = SignUpSerilizer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            try:
                Signup.objects.update_or_create(user_id=request.data['user_id'],defaults=request.data)
            # serializer.save()
                return Response({'status': "success", 'users': serializer.data, 'status_code': status.HTTP_201_CREATED},
                            status=status.HTTP_201_CREATED)
            except Exception as e:
                dict = {'msg': serializer.errors, 'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"}
                return Response(dict, status=status.HTTP_400_BAD_REQUEST)

        dict = {'msg': serializer.errors, 'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"}
        return Response(dict, status=status.HTTP_400_BAD_REQUEST)



class DeleteRecord(generics.GenericAPIView):
    queryset = Signup.objects.all()
    serializer_class = SignUpSerilizer

    def post(self, request, *args, **kwargs):
        print request.data['user_id']
        try:
            obj =Signup.objects.get(user_id=request.data['user_id'])
            obj.delete()
            return Response({'status': "success", 'msg': "Record deleted successfully", 'status_code': status.HTTP_204_NO_CONTENT},
                        status=status.HTTP_201_CREATED)
        except Exception as e:
            print e.message
            return Response("erro", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def create_list(request):
    """
    List all tasks, or create a new task.
    """

    if request.method == 'GET':

        tasks = Signup.objects.all()
        serializer = SignUpSerilizer(tasks, many=True)
        return Response({'status': "success", 'users': serializer.data, 'status_code':status.HTTP_201_CREATED})

    elif request.method == 'POST':
        unique_id = get_random_string(length=32)
        request.data['access_token'] = unique_id
        request.data['password'] =  base64.b64encode(request.data['password'])
        serializer = SignUpSerilizer(data=request.data)

        validate_str = validate_email(request.data,"")
        if validate_str != "":
            return Response({'msg': validate_str, 'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"})

        if serializer.is_valid():
            serializer.save()
            user = Signup.objects.get(email_id=request.data['email_id'], password=request.data['password'])
            obj_serializer = UpdateUserSerilizer(user)
            return Response({'status': "success", 'users': obj_serializer.data, 'status_code':status.HTTP_201_CREATED})
        else:
            return Response({'msg':serializer.errors,'status_code':status.HTTP_400_BAD_REQUEST,'status': "fail"})



@api_view(['GET', 'PUT', 'DELETE'])
def user_details(request,pk):

    try:
        user = Signup.objects.get(pk=pk)

        token_str = check_Token(user,request)

        if token_str != "":
            return Response({'msg':token_str,'status_code':status.HTTP_400_BAD_REQUEST,'status': "fail"})
    except:
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
            return Response({'msg':serializer.errors,'status_code':status.HTTP_400_BAD_REQUEST,'status': "fail"})

    elif request.method == 'DELETE':
        user.image.delete()
        user.delete()
        return Response({'status': "success", 'msg': "Record Deleted Successfully", 'status_code':status.HTTP_200_OK})



@api_view(['GET','POST'])
def user_login(request):
    if request.method == "POST":

        email = request.data['email_id']
        password = base64.b64encode(request.data['password'])

        try:
            user = Signup.objects.get(email_id=email,password=password)
            if user:
                user.access_token = get_random_string(length=32)
                user.device_token = request.data['device_token']
                user.device_type = request.data['device_type']
                user.save(update_fields=["access_token","device_type","device_token"])

                serializer = CreateUserSerilizer(user)
                push_notification(user.device_token)
                return Response({'status': "success", 'users': serializer.data, 'status_code': status.HTTP_200_OK})
            else:
                return Response({'msg':"Invalid credentials",'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"})

        except Exception as e:
            print e
            return Response({'msg': "This username/email is not valid",'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"})


@api_view(['GET'])
def user_logout(request,pk):

    try:
        user = Signup.objects.get(pk=pk)
        token_str = check_Token(user, request)

        if token_str != "":
            return Response({'msg': token_str, 'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"})

    except:
        return Response({'msg': "Invalid data", 'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"})

    if request.method == "GET":
        if user:

            try:
                user.access_token = ""
                user.device_token = ""
                user.device_type = ""
                user.save(update_fields=["access_token","device_type","device_token"])
                return Response({'status': "success", 'msg':"User logout successfully.", 'status_code': status.HTTP_200_OK})
            except:
                return Response({'msg': "Invalid data", 'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"})





@api_view(['POST'])
def update_deviceToken(request,pk):
    try:
        user = Signup.objects.get(pk=pk)
        token_str = check_Token(user, request)

        if token_str != "":
            return Response({'msg': token_str, 'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"})

    except:
        return Response({'msg': "Invalid data", 'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"})

    if request.method == "POST":
        if user:

            try:
                user.device_token = request.data['device_token']
                user.device_type = request.data['device_type']
                user.save(update_fields=["device_type","device_token"])
                return Response({'status': "success", 'msg':"Device Token updated successfully.", 'status_code': status.HTTP_200_OK})
            except:
                return Response({'msg': "Invalid data", 'status_code': status.HTTP_400_BAD_REQUEST, 'status': "fail"})


def push_notification(apns_token):
    # queryset = APNSDevice.objects.get_queryset().values_list()
    # print queryset
    # APNSDevice.objects.create(registration_id=apns_token)

    device = APNSDevice.objects.get(registration_id=apns_token)
    # device = APNSDevice(registration_id=apns_token)
    device.send_message("You've got mail", badge=1, extra={"foo": "bar"})  # Silent message with badge and added custom data.

