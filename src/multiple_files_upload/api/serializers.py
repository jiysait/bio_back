from rest_framework import serializers

from multiple_files_upload.models import MyFile


class MultipleFilesUploadSerializer(serializers.Serializer):

    files = serializers.ListField(child=serializers.FileField(
        max_length=1000000, allow_empty_file=False, use_url=False))

    def create(self, validated_data):
        results = []
        files = validated_data.pop('files')
        for afile in files:
            results.append(MyFile.objects.create(file=afile))
        return results
