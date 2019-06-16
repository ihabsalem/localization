from .models import Language
from rest_framework import serializers

class LanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ("name", "code")