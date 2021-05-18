from django.conf.urls import url
from .views import OCRView

app_name = 'ocr'

urlpatterns = [
    url('api/ocr_service/$', OCRView.as_view(), name='image_ocr_service'),
]
