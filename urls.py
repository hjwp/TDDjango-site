from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import include, patterns, url
from django.http import HttpResponsePermanentRedirect

from tddjango_site.tutorials import views as tutorial_views
from tddjango_site.blog import views as blog_views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', tutorial_views.tutorial, name='home'),
    url(r'^tutorial/(\d+)/$', tutorial_views.tutorial, name='tutorial'),

    url(r'^blog/$', blog_views.blog, name='blog'),

    url(r'^blog/articles/2013/test-driven-development-web-applications-book-exis/', lambda r: HttpResponsePermanentRedirect("http://www.obeythetestinggoat.com/tdd-web-programming-book-on-oreilly-early-release.html")),
    url(r'^blog/articles/2013/next-stage-writing-book/', lambda r: HttpResponsePermanentRedirect("http://www.obeythetestinggoat.com/writing-a-book-announcement.html")),


    url(r'^blog/articles/', include('articles.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
# static files via django - not ideal
urlpatterns += staticfiles_urlpatterns()
