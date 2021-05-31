from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser

from ebs.api.serializers import AnalysisSerializer, SequenceSerializer
from ebs.models import Analysis, Sequence


@api_view(['POST', ])
@parser_classes([MultiPartParser])
def open_analysis_view(request):
    if request.method == 'POST':
        serializer = AnalysisSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
def read_all_analyses_view(request):
    try:
        analyses = Analysis.objects.all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AnalysisSerializer(analyses, many=True)
        return Response(serializer.data)


@api_view(['POST', ])
@parser_classes([MultiPartParser])
def add_sequence_view(request):
    if request.method == 'POST':
        flag = 1
        files = request.data.pop('files')
        for file in files:
            dict = {}
            dict['seqfile_path'] = file
            serializer = SequenceSerializer(data=dict)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            else:
                flag = 0

        if flag == 1:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
def read_all_sequences_view(request):
    try:
        sequences = Sequence.objects.all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SequenceSerializer(sequences, many=True)
        return Response(serializer.data)
