from django.conf.urls import url

from .views import create_comment, delete_comment, get_comment_info

urlpatterns = [
    url(r'^create(/)?', create_comment),
    url(r'^info/(?P<pk>\d+)(/)?$', get_comment_info),
    url(r'^delete/(?P<pk>\d+)(/)?$', delete_comment),
]
