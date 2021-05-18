from django.conf.urls import url
from .views import UserDetailView, EachUserDetailView, BillView, EachBillView

app_name = 'user_details'

urlpatterns = [
    url('api/user_detail/$', UserDetailView.as_view(), name='user_detail'),
    url('api/user_detail/(?P<id>[0-9]+)/$', EachUserDetailView.as_view(), name='each_user_detail'),
    url('api/bill/$', BillView.as_view(), name='bill_detail'),
    url('api/bill/(?P<id>[0-9]+)/$', EachBillView.as_view(), name='each_bill_detail'),
]
