from django.conf.urls import url

from .views import create_task, get_task_info, update_task, delete_task, get_filtered_tasks

urlpatterns = [
    url(r'^create(/)?$', create_task),
    url(r'^info/(?P<pk>\d+)(/)?$', get_task_info),
    url(r'^update/(?P<pk>\d+)(/)?$', update_task),
    url(r'^delete/(?P<pk>\d+)(/)?$', delete_task),
    url(r'^filter(/)?$', get_filtered_tasks),
]
