from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^$', 'HackatonFacebook.recipe.views.home', name=u'home'),
    url(r'^recipes$', 'HackatonFacebook.recipe.views.recipes_list', name=u'recipes_list'),
    url(r'^recipe/new$', 'HackatonFacebook.recipe.views.recipe_create_update', name=u'recipe_create_update'),
    url(r'^like$', 'HackatonFacebook.recipe.views.like', name=u'like'),
    url(r'^favoritos$', 'HackatonFacebook.recipe.views.favoritos', name=u'favoritos'),
    url(r'^test/home', 'HackatonFacebook.recipe.views.test_home', name='test_home'),
    url(r'^test/details/(?P<pk>\d+)', 'HackatonFacebook.recipe.views.test_details', name='test_details'),
    url(r'^imprimir/(?P<pk>\d+)', 'HackatonFacebook.recipe.views.imprimir', name='imprimir'),
    url(r'^user/favorites/$', 'HackatonFacebook.recipe.views.user_favorites', name='user-favorites'),
)
