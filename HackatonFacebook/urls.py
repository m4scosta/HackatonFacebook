from django.conf.urls import patterns, include, url
from django.contrib import admin

_BASE_VIEW = 'HackatonFacebook.views'
_BASE_AJAX = 'HackatonFacebook.core'


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', '%s.home.home' % _BASE_VIEW),
    url(r'^', include('HackatonFacebook.recipe.urls')),
    url(r'^$/recei', '%s.home.home' % _BASE_VIEW)
    # url(r'^$', include('HackatonFacebook.recipe.urls'))
)
