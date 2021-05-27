import json
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser

from .serializers import MultipleFilesUploadSerializer


# You can choose one of approaches to handle HTTP Requests

# Function Based Views
# This approach is not commonly used, but it is much more straightforward.
@api_view(['POST', ])
@parser_classes([MultiPartParser])
def multiple_files_upload_view(request):
    if request.method == 'POST':
        serializer = MultipleFilesUploadSerializer(
            data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Class Based Views
