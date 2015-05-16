from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^$', 'HackatonFacebook.recipe.views.home', name=u'home'),
)
