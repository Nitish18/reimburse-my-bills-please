from django.conf.urls import url
from .views import UserDetailView, EachUserDetailView

app_name = 'user_details'

urlpatterns = [
    url('api/user_detail/$', UserDetailView.as_view(), name='user_detail'),
    url('api/user_detail/(?P<id>[0-9]+)/$', EachUserDetailView.as_view(), name='each_user_detail'),
]
