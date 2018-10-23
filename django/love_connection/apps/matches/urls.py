from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.index, name="index"),
    url(r'^create/$', views.create, name="create"),
    # url(r'^new/$', views.new, name="new"),
    # url(r'^(?P<id>\d+)/update/$', views.update, name="update"),
    url(r'^delete/$', views.delete, name="delete"),
    # url(r'^(?P<id>\d+)/edit/$', views.edit, name="edit"),
    # url(r'^(?P<id>\d+)/$', views.show, name="show"),
]