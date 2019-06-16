from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Source
from .serializers import SourceSerializer

# Create your tests here.
class BaseApiViewTest(APITestCase):
    client = APIClient()
    
    @staticmethod
    def add_Source(name=""):
        if name != "":
            Source.object.create(name= name);
            return

    def setup(self):
        self.add_Source("IPAD")
        self.add_Source("DASHBOARD")



class GetAllSources(BaseApiViewTest):
    def test_get_all_languages(self):
        response = self.client.get(
            reverse("sources-all", kwargs={"version": "v1"}))
        expected = Source.objects.all()
        serialized = SourceSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
