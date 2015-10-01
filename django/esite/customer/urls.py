from django.conf.urls import patterns, url

from customer import views

urlpatterns = patterns('',

    # ex: /page/about/
    url(r'^list/$', views.get_customers, name='get_customers'),
#     url(r'^vehicle/(?P<oid>\S+)/$', views.vehicle, name='vehicle'),
    
)