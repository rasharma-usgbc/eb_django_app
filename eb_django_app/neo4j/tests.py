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
        
class BuildingAPITest(BuildingTestCase):

    def test_read(self):
        # self.c.login("username", "password")
        building_url = self.base
        
        # Retrieve created building
        r = self.c.get(building_url); #, auth=(self.u, self.p))
        
        # Run tests
        self.assertEqual(r.status_code, 200)
        print(r.content)
        buildings_json = json.loads(r.content)
        self.assertNotEqual(len(buildings_json), 0)
        # self.assertJSONEqual(r.json(), '{"name": "USGBC", "address":"2101 L Street", "leed_id": 1000000117, "certification": "platinum"}')
        #test comment 1
        #test comment 2
