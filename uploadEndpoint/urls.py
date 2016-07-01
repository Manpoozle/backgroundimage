from django.conf.urls import url

from . import uploadEndpoint

urlpatterns = [
    url(r'^$', uploadEndpoint.upload_video, name='uploadEndpoint'),
]