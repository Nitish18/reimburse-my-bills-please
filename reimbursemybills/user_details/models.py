import logging
from django.db import models
from django.contrib.auth.models import User

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
