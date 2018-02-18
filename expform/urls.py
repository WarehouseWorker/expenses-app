from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.exp_list, name='exp_list'),
    url(r'^exp/(?P<pk>[0-9]+)/$', views.exp_detail, name='exp_detail'),
    url(r'^exp/new/$', views.exp_new, name='exp_new'),
]