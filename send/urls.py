from django.conf.urls import url, include

from .views import UploadView

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'send', UploadView)

urlpatterns = [
    url(r'', include(router.urls)),
]
