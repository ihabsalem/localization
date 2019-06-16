from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.shortcuts import render
from .models import Language
from .serializers import LanguagesSerializer
from rest_framework.response import Response
from rest_framework.views import status
# Create your views here.


class LanguagesListView(APIView):
    """
    Provides a get method handler.
    """
    queryset = Language.objects.all()
    serializer_class = LanguagesSerializer


@api_view(["GET"])
def post(self, request, *args, **kwargs):
    language = Language.objects.all()
    return Response(
        data=LanguagesSerializer(language).data,
        status=status.HTTP_201_CREATED
    )

@api_view(["POST"])
def post(self, request, *args, **kwargs):
    language = Language.objects.creat(
        name=request.data["name"], code=request.data["code"])
    return Response(
        data=LanguagesSerializer(language).data,
        status=status.HTTP_200_OK
    )


