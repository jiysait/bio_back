from rest_framework import serializers

from multiple_files_upload.models import MyFile


class MultipleFilesUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyFile
        fields = '__all__'
