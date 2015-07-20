import requests
from django.test import TestCase
import json

class BuildingCrudTestCase(TestCase):

    endpoint = "http://localhost:8080/"
    u = ""
    p = ""

    def setUp(self):
        # Create building, add to DB
        print("Read setUp")
    
    def test_read(self):
        # Retrieve created building
        path = "get/building"
        r = requests.get(self.endpoint + path); #, auth=(self.u, self.p))
        
        # Run tests
        self.assertContains(r, "", status_code=200)
        self.assertJSONEqual(r.json(), '{"name": "USGBC", "address":"2101 L Street", "leed_id": 1000000117, "certification": "platinum"}')
       
    def tearDown(self):
        # Delete created building
        print "Read tearDown"
