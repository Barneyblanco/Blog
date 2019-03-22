from django.conf.urls import url
from . import views

app_name = 'forum'

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	url(r'post/add/$', views.PostCreate.as_view(), name='post-add'),
	url(r'post/(?P<pk>[0-9]+)/$', views.PostUpdate.as_view(), name='post-update'),
	url(r'post/(?P<pk>[0-9]+)/delete/$', views.PostDelete.as_view(), name='post-delete'),
	]
	
