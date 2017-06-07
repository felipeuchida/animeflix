from django.conf.urls import url
from . import views

app_name = 'video'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'series/add/$', views.SeriesCreate.as_view(), name='series-add'),
    url(r'series/(?P<pk>[0-9]+)/$', views.SeriesUpdate.as_view(), name='series-update'),
    url(r'series/(?P<pk>[0-9]+)/delete/$', views.SeriesDelete.as_view(), name='series-delete'),
]
