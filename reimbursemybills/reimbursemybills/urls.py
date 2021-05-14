
from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^dashboard/', include('dashboard_api.urls', namespace='user_dashboard')),
    url(r'^ocr/', include('ocr.urls', namespace='ocr')),
    url(r'^user_auth/', include('user_authentication.urls', namespace='user_auth')),
    url(r'^user_details/', include('user_details.urls', namespace='user_details')),
    url(r'^admin/', admin.site.urls),
]
