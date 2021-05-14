
import logging

from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_404_NOT_FOUND,\
    HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserDetailSerializer
from .models import UserDetail

logger = logging.getLogger(__name__)


class UserDetailView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user_details = UserDetail.objects.all()
        return Response({
            'message': "success",
            'data': UserDetailSerializer(user_details, many=True).data
        }, HTTP_200_OK)

    def post(self, request):
        try:
            data = request.data
            # getting user info
            user_id = data.get('user_id')
            if not user_id:
                return Response({
                    'message': "User id info not provided",
                }, status=HTTP_400_BAD_REQUEST)
            serializer = UserDetailSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'message': "success",
                    'data': serializer.validated_data
                }, status=HTTP_201_CREATED)
            return Response({
                'message': "LOL",
            }, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'message': str(e),
            }, status=HTTP_500_INTERNAL_SERVER_ERROR)


class EachUserDetailView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, id):
        user_detail = UserDetail.objects.filter(id=id).first()
        return Response({
            'message': "success",
            'data': UserDetailSerializer(user_detail).data
        }, HTTP_200_OK)

    def patch(self, request, id):
        """
        """
        user_detail_obj = UserDetail.objects.filter(id=id).first()
        data = request.data
        serializer = UserDetailSerializer(user_detail_obj, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': "success",
                'data': serializer.data
            }, status=HTTP_200_OK)
        return Response({
            'message': serializer.errors}, status=HTTP_400_BAD_REQUEST
        )
