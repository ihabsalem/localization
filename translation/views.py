from django.shortcuts import render
from rest_framework import generics
from .models import Translation
from .serializers import TranslationSerializer

# Create your views here.
class TranslationListView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer