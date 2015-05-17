from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^$', 'HackatonFacebook.recipe.views.home', name=u'home'),




    url(r'^test/home', 'HackatonFacebook.recipe.views.test_home', name='test_home'),
    url(r'^test/details/(?P<pk>\d+)', 'HackatonFacebook.recipe.views.test_details', name='test_details'),
)
