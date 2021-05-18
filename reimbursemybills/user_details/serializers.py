import logging
from rest_framework import serializers
from .models import UserDetail, Bill
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)


class UserDetailSerializer(serializers.Serializer):
    """
    """
    id = serializers.IntegerField(required=False)
    user = serializers.SerializerMethodField()
    pan_number = serializers.CharField(required=False)
    bank_account_number = serializers.CharField(required=False)
    ifsc_code = serializers.CharField(required=False)
    bank_name = serializers.CharField(required=False)
    swiggy_auth_token = serializers.CharField(required=False)
    zomato_auth_token = serializers.CharField(required=False)
    cultfit_auth_token = serializers.CharField(required=False)
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)

    def get_user(self, obj):
        return obj.user.email

    def create(self, validated_data):
        user = User.objects.get(id=self.initial_data['user_id'])
        validated_data["user"] = user
        return UserDetail.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        """
        instance.pan_number = validated_data.get("pan_number", instance.pan_number)
        instance.bank_account_number = validated_data.get("bank_account_number", instance.bank_account_number)
        instance.ifsc_code = validated_data.get("ifsc_code", instance.ifsc_code)
        instance.bank_name = validated_data.get("bank_name", instance.bank_name)
        instance.swiggy_auth_token = validated_data.get("swiggy_auth_token", instance.swiggy_auth_token)
        instance.zomato_auth_token = validated_data.get("zomato_auth_token", instance.zomato_auth_token)
        instance.cultfit_auth_token = validated_data.get("cultfit_auth_token", instance.cultfit_auth_token)

        instance.save()
        return instance


class BillSerializer(serializers.Serializer):
    """
    """
    id = serializers.IntegerField(required=False)
    user = serializers.SerializerMethodField()

    city = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    date = serializers.CharField(required=False)
    total_amount = serializers.IntegerField(required=False)
    bill_type = serializers.CharField(required=False)
    storage_link = serializers.UUIDField(required=False)

    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)

    def get_user(self, obj):
        return obj.user.email

    def create(self, validated_data):
        user = User.objects.get(id=self.initial_data['user_id'])
        validated_data["user"] = user
        return UserDetail.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        """
        instance.city = validated_data.get("city", instance.city)
        instance.name = validated_data.get("name", instance.name)
        instance.date = validated_data.get("date", instance.date)
        instance.total_amount = validated_data.get("total_amount", instance.total_amount)

        instance.save()
        return instance
