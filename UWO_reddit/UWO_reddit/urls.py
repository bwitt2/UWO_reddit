from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from UWO_reddit_app import views

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', views.index, name='index'),
                       url(r'^display/(\d+)/$', views.display),
                       )
