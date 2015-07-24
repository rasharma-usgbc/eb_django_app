from django.test import TestCase
from neo4j.models import Buildings
from neo4j.views import buildings
from django.test.client import RequestFactory

class BuildingTestCase(TestCase):
    def setUp(self):
        Buildings.objects.create(name="test_name")
        self.factory = RequestFactory()

    def test_read_success(self):
        """Building read is verified"""
        request = self.factory.get('/buildings')
        response = buildings(request)
        self.assertEqual(response.status_code, 200)
        b = Buildings.objects.get(pk=1)
        self.assertEqual(b.name, "test_name")
