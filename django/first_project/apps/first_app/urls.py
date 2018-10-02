from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name="index"),
  url(r'^first_app/new_route/$', views.new_route, name="new_route"),
]