from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'main.views.index'),
    url(r'^logout/$', 'main.views.logout_page', name="logout"),
    url(r'^admin/', include(admin.site.urls)),
) + staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
