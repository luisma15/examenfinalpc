from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.listarp),
        url(r'^post/new/$', views.post_new, name='post_new'),
    ]
