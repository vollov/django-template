from django.conf.urls import patterns, url

from account import views

urlpatterns = patterns('',

    # ex: /account/register/
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
#     url(r'^vehicle/(?P<oid>\S+)/$', views.vehicle, name='vehicle'),
    
)