import requests
from django.test import TestCase
import json

from django.test.client import Client
from django.contrib.auth.models import User

def get_test_user():
    u = User(username="username", is_superuser=True)
    u.set_password("password")
    u.save()
    return u

def get_test_building():
    b = models.Building(leed_id=11, name="Test Name", address="Test Address", certification="diamond")
    b.save()
    return b

class BuildingTestCase(TestCase):
    def setUp(self):
        # Create building, add to DB
        # self.u = get_test_user()
        # self.b = get_test_building()
        self.c = Client()
        self.base = '/building/'
        
