from django.urls import path
from .views import LanguagesListView

urlpatterns = [
    path('', LanguagesListView.as_view(), name="language-all")
]