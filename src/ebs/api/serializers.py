from rest_framework import serializers

from ebs.models import Analysis, Sequence


class SequenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sequence
        fields = '__all__'


class AnalysisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Analysis
        fields = '__all__'
        depth = 1
