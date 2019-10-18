from django.test import TestCase
from rest_framework.test import APIRequestFactory
from django.db.models.query import QuerySet

from .models import Scoters
from .views import ScoterListView


class ScoterListViewTestCase(TestCase):
    def setUp(self):
        # Create a test data
        self.scoter = Scoters.objects.create(lat=37.788548, lng=-122.411548)

    def tearDown(self):
        pass

    def test_scoter_view_1(self):
        """
        Test without lat,lng and radius parms

        """
        api_request = APIRequestFactory().get("/available")
        list_view = ScoterListView.as_view({'get': 'list'})
        response = list_view(api_request)
        self.assertEqual(response.status_code, 200)

    def test_scoter_view_2(self):
        """
        Test with lat,lng and radius parms

        """
        api_request = APIRequestFactory().get(
            "/navailable/?lat=37.788548&lng=-122.411548&radius=25")
        list_view = ScoterListView.as_view({'get': 'list'})
        response = list_view(api_request)
        self.assertEqual(response.status_code, 200)
