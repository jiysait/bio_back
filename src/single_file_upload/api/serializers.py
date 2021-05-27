from rest_framework import serializers

from single_file_upload.models import MyFile


class SingleFileUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyFile
        fields = ('file', )
