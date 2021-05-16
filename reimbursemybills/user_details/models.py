import logging
from django.db import models
from django.contrib.auth.models import User
from .constants import BILL_TYPE_CHOICES

logger = logging.getLogger(__name__)


class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    pan_number = models.CharField(null=True, default="", blank=True, max_length=25)
    bank_account_number = models.CharField(null=True, default="", blank=True, max_length=25)
    ifsc_code = models.CharField(null=True, default="", blank=True, max_length=25)
    bank_name = models.CharField(null=True, default="", blank=True, max_length=25)
    swiggy_auth_token = models.CharField(null=True, default="", blank=True, max_length=200)
    zomato_auth_token = models.CharField(null=True, default="", blank=True, max_length=200)
    cultfit_auth_token = models.CharField(null=True, default="", blank=True, max_length=200)
    created_at = models.DateTimeField('Date created', auto_now_add=True)
    updated_at = models.DateTimeField('Date updated', auto_now=True)

    class Meta:
        verbose_name = 'User Detail'

    def __str__(self):
        return f"User Detail- id: {self.pk}, user: {self.user.email}"

    def __repr__(self):
        return f"User Detail- id: {self.pk}, user: {self.user.email}"


class Bill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Date created', auto_now_add=True)
    updated_at = models.DateTimeField('Date updated', auto_now=True)

    city = models.CharField(null=True, default="", blank=True, max_length=25)
    name = models.CharField(null=True, default="", blank=True, max_length=25)
    date = models.CharField(null=True, default="", blank=True, max_length=25)
    total_amount = models.IntegerField(null=True, blank=True)
    bill_type = models.CharField(choices=BILL_TYPE_CHOICES, max_length=30)

    class Meta:
        verbose_name = 'User Bill Detail'

    def __str__(self):
        return f"Bill Detail- id: {self.pk}, user: {self.user.email}, type: {self.bill_type}"

    def __repr__(self):
        return f"Bill Detail- id: {self.pk}, user: {self.user.email}, type: {self.bill_type}"
