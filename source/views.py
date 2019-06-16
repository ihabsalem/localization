from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import Source
from .serializers import SourceSerializer
from django.shortcuts import get_object_or_404
# Create your views here.
class SourceListView(generics.ListAPIView):
    """
    Provides a get method handler.
    """

    def get(self, request, *args, **kwargs):
        source = Source.objects.all()
        print(source)
        serializer_class = SourceSerializer(source, many=True)
        return Response(data=serializer_class.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = SourceSerializer(data=request.data)
        print("Sourceeee")
        if Source.objects.filter(name=request.data["name"]).exists():
            return Response(
                {"success": "Source already exists"}, status=status.HTTP_409_CONFLICT
            )

        if serializer.is_valid():
            Source_saved = serializer.save()
            return Response(
                {
                    "success": "Source '{}' created successfully".format(
                        Source_saved.name
                    )
                }
            )

    def delete(self, request, *args, **kwargs):
        source = get_object_or_404(Source.objects.all(), name=kwargs["pk"])
        source.delete()
        return Response(status=status.HTTP_200_OK)
