from django.urls import path
from .views import SourceListView

urlpatterns = [
    path("", SourceListView.as_view(), name="sources-all"),
    path("/<pk>", SourceListView.as_view(), name="sources-action"),
]

