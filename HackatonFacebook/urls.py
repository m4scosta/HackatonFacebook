from django.conf.urls import patterns, include, url
from django.contrib import admin

_BASE_VIEW = 'HackatonFacebook.views'
_BASE_AJAX = 'HackatonFacebook.core'

urlpatterns = patterns('',
    url(r'/get/teste', '%s.usecase.ajax.get_by_ajax' % _BASE_AJAX)
)

urlpatterns += patterns('',
    # Examples:
    # url(r'^$', 'HackatonFacebook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^ajax/', '%s.ajax.ajax.home' % _BASE_VIEW)
)
