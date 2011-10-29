from django.conf.urls.defaults import patterns, url
from tddjango_site.tutorials import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tddjango_site.views.home', name='home'),
    url(r'^$', views.tutorial, name='home'),
    url(r'^tutorial/(\d+)/$', views.tutorial, name='tutorial'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
