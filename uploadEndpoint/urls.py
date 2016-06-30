from django.conf.urls import url

from . import uploadEndpoint

urlpatterns = [
    url(r'^$', uploadEndpoint.index, name='index'),
]