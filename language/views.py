from rest_framework.views import APIView
from .models import Language
from .serializers import LanguagesSerializer
from rest_framework.response import Response
from rest_framework.views import status
from django.shortcuts import get_object_or_404


class LanguagesListView(APIView):
    """
    Provides a get method handler.
    """

    def get(self, request, *args, **kwargs):
        language = Language.objects.all()
        print(language)
        serializer_class = LanguagesSerializer(language, many=True)
        return Response(data=serializer_class.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = LanguagesSerializer(data=request.data)

        if (
            Language.objects.filter(code=request.data["code"]).exists()
            or Language.objects.filter(name=request.data["name"]).exists()
        ):
            return Response(
                {"success": "language already exists"}, status=status.HTTP_409_CONFLICT
            )

        if serializer.is_valid():
            language_saved = serializer.save()
            return Response(
                {
                    "success": "Language '{}' created successfully".format(
                        language_saved.name
                    )
                }
            )

    def delete(self, request, *args, **kwargs):
        language = get_object_or_404(Language.objects.all(), code=kwargs["pk"])
        language.delete()
        return Response(status=status.HTTP_200_OK)
