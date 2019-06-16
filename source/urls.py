from django.urls import path
from .views import SourceListView

urlpatterns = [
    path('', SourceListView.as_view(), name="sources-all")
]