from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import include, patterns, url

from tddjango_site.tutorials import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.tutorial, name='home'),
    url(r'^tutorial/(\d+)/$', views.tutorial, name='tutorial'),

    url(r'^blog/', include('articles.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
# static files via django - not ideal
urlpatterns += staticfiles_urlpatterns()
