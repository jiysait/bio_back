from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from single_file_upload.models import SingleFileUpload

from .serializers import SingleFileUploadSerializer


@api_view(['POST', ])
def single_file_upload_view(request):
    if request.method == 'POST':
        serializer = SingleFileUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
