# myapp/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import Base64FileSerializer
from django.conf import settings
import os

class Base64FileUploadView(APIView):
    def post(self, request):
        serializer = Base64FileSerializer(data=request.data)
        if serializer.is_valid():
            # Get the saved file name from the serializer
            file_name = serializer.validated_data['file']
            file_url = os.path.join(settings.MEDIA_URL, file_name)

            return Response({"file_url": file_url}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
