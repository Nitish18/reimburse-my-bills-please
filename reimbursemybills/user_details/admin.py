
import logging
from django.contrib import admin
from .models import UserDetail

logger = logging.getLogger(__name__)


class UserDetailAdmin(admin.ModelAdmin):
    """
    """
    list_filter = ()
    list_display = ('user', 'pan_number', 'bank_account_number', 'ifsc_code', 'bank_name', 'created_at',
                    'updated_at', 'swiggy_auth_token', 'zomato_auth_token', 'cultfit_auth_token')
    readonly_fields = ()

admin.site.register(UserDetail, UserDetailAdmin)
