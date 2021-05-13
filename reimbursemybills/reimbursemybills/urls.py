
from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^user_auth/', include('user_authentication.urls', namespace='user_auth')),
    url(r'^admin/', admin.site.urls),
]
