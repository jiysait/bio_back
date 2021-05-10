from rest_framework import serializers
from .models import tRNA

class tRNASerializer(serializers.ModelSerializer):
    class Meta:
        model = tRNA
        fields = ('gene', 'contig', 'start', 'end', 'length')