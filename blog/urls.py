from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<article_id>\d+)/$', views.single_post, name='single_post')
]