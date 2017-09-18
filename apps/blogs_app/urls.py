from django.conf.urls import url,include
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index)  ,
    url(r'^new$', views.new),   # This line has changed!
    url(r'^create$', views.create),
    url(r'^(?P<blog_id>\d+)$', views.show),
    url(r'^(?P<blog_id>\d+)/edit$', views.edit),
    url(r'^(?P<blog_id>\d+)/delete$', views.delete)
  ]