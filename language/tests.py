from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Language
from django.urls import reverse
from .serializers import LanguagesSerializer

# Create your tests here.


class BaseApiViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def add_lanuage(name="", code=""):
        if name != "" and code != "":
            Language.objects.create(name=name, code=code)
            return

    def setup(self):
        self.addLanuage("English", "en")
        self.addLanuage("Arabic", "ar")


class GetAllLanguages(BaseApiViewTest):
    def test_get_all_languages(self):
        response = self.client.get(
            reverse("language-all", kwargs={"version": "v1"}))
        expected = Language.objects.all()
        serialized = LanguagesSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
