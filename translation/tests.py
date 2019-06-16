from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from django.urls import reverse
from .models import Translation
from .serializers import TranslationSerializer
# Create your tests here.
class BaseApiViewTest(APITestCase):
    client = APIClient()
    
    @staticmethod
    def add_translation(source="",language="", key="", label=""):
        if key != "" and label != "":
            Translation.object.create(source=source, label = label, key = key);
            return

    def setup(self):
        self.add_translation("", 'HELLO', )


class GetAllSources(BaseApiViewTest):
    def test_get_all_languages(self):
        response = self.client.get(
            reverse("translations-all", kwargs={"version": "v1"}))
        expected = Translation.objects.all()
        serialized = TranslationSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
