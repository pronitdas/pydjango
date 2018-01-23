# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import generics
from .serializers import SignUpSerilizer
from .models import Signup
from rest_framework.response import Response
from rest_framework import status
import json
import re

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
        print request.data['user_id']
        try:
            obj = Signup.objects.filter(request.data['user_id']).update(request.data)
            return Response({'status': "success", 'users': "", 'status_code':status.HTTP_201_CREATED}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print e.message
            dict = {'msg':'error', 'status_code':status.HTTP_400_BAD_REQUEST,'status': "fail"}
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


