from .models import Language
from rest_framework import serializers


class LanguagesSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Language.objects.create(**validated_data)

    
    class Meta:
        model = Language
        fields = ("name", "code")
