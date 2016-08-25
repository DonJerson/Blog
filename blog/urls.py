from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),

	# url(r'^delete_candidate/(?P<candidate_id>\d+)/$', views.delete_candidate, name='delete_candidate'),
]