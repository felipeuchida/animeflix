from django.conf.urls import url
from . import views

app_name = 'video'

urlpatterns = [
	# /video/
    url(r'^$', views.index, name='index'),

    # /video/71/   71 é o id(exemplo)
    url(r'^(?P<series_id>[0-9]+)/$', views.detail, name='detail'),

    # /video/71/favorite   71 é o id(exemplo)
    url(r'^(?P<series_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
]
