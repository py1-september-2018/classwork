from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name="index"),
  url(r'^add_word/$', views.add_word, name="add_word"),
  url(r'^clear/$', views.clear, name="clear"),
  url(r'users/(?P<id>\d+)/show', views.show, name="show")
]