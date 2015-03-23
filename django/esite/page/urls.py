from django.conf.urls import patterns, url

from page import views

urlpatterns = patterns('',

    # ex: /page/about/
    url(r'^(?P<page_slug>\S+)/$', views.detail, name='detail'),
)