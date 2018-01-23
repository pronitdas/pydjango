# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from django.test import  TestCase
from .models import Signup

from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

# Create your tests here.

class ModelTestCase(TestCase):

    def setUp(self):
        self.userlist_name = "Write world class code"
        self.userlist = Signup(name = self.userlist_name)


    def test_model_can_create_a_bucketlist(self):
        old_count = Signup.objects.count()
        self.userlist.save()
        new_count = Signup.objects.count()
        self.assertNotEqual(old_count,new_count)


class ViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.signup_data = {'name': 'Go to Ibiza'}
        self.response = self.client.post(
            reverse('create'),
            self.signup_data,
            format="json")

    def test_api_can_create_a_signuplist(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

