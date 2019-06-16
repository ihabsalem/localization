from django.shortcuts import render
from rest_framework import generics
from .models import Source
from .serializers import SourceSerializer

# Create your views here.
class SourceListView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Source.objects.all()
    serializer_class = SourceSerializer