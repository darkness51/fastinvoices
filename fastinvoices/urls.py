from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import login
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from main.views import IndexView, ProductListView, ProductAddView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name="home"),
    url(r'^products/$', ProductListView.as_view(), name="product-list"),
    url(r'^products/add/$', ProductAddView.as_view(), name="product-add"),
    url(r'^login/$', 'django.contrib.auth.views.login', name="login"),
    url(r'^logout/$', 'main.views.logout_page', name="logout"),
    url(r'^admin/', include(admin.site.urls)),
) + staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
