# myapp/serializers.py

import base64
import uuid
import os
from django.core.files.base import ContentFile
from django.conf import settings
from rest_framework import serializers

class Base64FileSerializer(serializers.Serializer):
    file = serializers.CharField()  # This will hold the base64 string

    def validate_file(self, value):
        # Ensure the data is in the expected base64 format
        if not value.startswith('data:'):
            raise serializers.ValidationError("Invalid base64 format.")

        # Split and decode the base64 data
        format, base64_str = value.split(';base64,')
        file_ext = format.split('/')[-1]  # Extract file extension from format
        file_data = base64.b64decode(base64_str)

        # Generate a unique filename
        file_name = f"{uuid.uuid4()}.{file_ext}"

        # Create ContentFile and save it to the media directory
        content_file = ContentFile(file_data, name=file_name)

        # Define the full path for saving
        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
        with open(file_path, 'wb') as f:
            f.write(content_file.read())  # Write the decoded content to the file

        return file_name  # Return the saved file name
