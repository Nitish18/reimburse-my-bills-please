
import logging

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_404_NOT_FOUND,\
    HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)


class UserAuthTest(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        return Response({
            'message': "success",
            'data': "dummy data"
        }, HTTP_200_OK)


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
