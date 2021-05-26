from rest_framework import serializers

from single_file_upload.models import SingleFileUpload


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = SingleFileUpload
        fields = ('name', 'file')
