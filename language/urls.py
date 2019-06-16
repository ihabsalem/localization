from django.urls import path
from .views import LanguagesListView
from rest_framework import routers


# router = routers.DefaultRouter(trailing_slash = False)
# router.register ("", LanguagesListView)


# urlpatterns = router.urls

urlpatterns = [
    path("", LanguagesListView.as_view(), name="language-all"),
    path('/<pk>', LanguagesListView.as_view(), name="language-action")
]
