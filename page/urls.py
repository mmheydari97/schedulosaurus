from django.conf.urls import url

from page import views

app_name = 'page'

urlpatterns = [
    url(r'^$', views.initial, name='initial'),
    url(r'^(?P<packet_id>\d+$)', views.add_new_task, name='add_new_task'),
    url(r'^new_packet$', views.add_new_packet, name='add_new_packet'),
    url(r'^end_task/(?P<task_id>\d+$)', views.end_task, name='end_task'),
]