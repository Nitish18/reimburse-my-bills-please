
import logging
from django.contrib import admin
from .models import UserDetail, Bill

logger = logging.getLogger(__name__)


class UserDetailAdmin(admin.ModelAdmin):
    """
    """
    list_filter = ()
    list_display = ('user', 'pan_number', 'bank_account_number', 'ifsc_code', 'bank_name', 'created_at',
                    'updated_at', 'swiggy_auth_token', 'zomato_auth_token', 'cultfit_auth_token')
    readonly_fields = ()


class BillAdmin(admin.ModelAdmin):
    """
    """
    list_filter = ('bill_type', 'city')
    list_display = ('user', 'name', 'bill_type', 'date', 'total_amount', 'city',
                    'updated_at', 'created_at')
    search_fields = ('user__email', 'city')
    readonly_fields = ()


admin.site.register(UserDetail, UserDetailAdmin)
admin.site.register(Bill, BillAdmin)
