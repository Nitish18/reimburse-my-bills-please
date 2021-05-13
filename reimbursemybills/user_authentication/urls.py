from django.conf.urls import url
from .views import UserAuthTest, UserRegistrationView
from rest_framework_simplejwt import views as jwt_views

app_name = 'user_authentication'

urlpatterns = [
    url(r'^api/test/$', UserAuthTest.as_view()),
    url(r'^api/register/$', UserRegistrationView.as_view()),
    url('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
