
import logging

from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_404_NOT_FOUND,\
    HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FileUploadParser
from .ocr_engine import OCREngine


class OCRView(APIView):
    permission_classes = (IsAuthenticated, )
    parser_classes = (FileUploadParser, )

    def post(self, request):
        user = request.user
        bill_source_type = request.GET.get('bill_source_type', 'physical')

        img_file_bytes = request.FILES["file"].read()

        # analyzing image
        ocr_obj = OCREngine(bill_source=bill_source_type)
        ocr_output = ocr_obj.analyze_image(img_file_bytes)

        return Response({
            'message': "success",
            'date': ocr_output
        }, HTTP_200_OK)
