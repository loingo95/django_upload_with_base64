# myapp/urls.py

from django.urls import path
from .views import Base64FileUploadView

urlpatterns = [
    path('upload/', Base64FileUploadView.as_view(), name='upload-file'),
]
