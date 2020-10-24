from django.conf.urls import url
from . import views

app_name = 'beerlist'

urlpatterns = [
    # /beerlist/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /beerlist/541/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /beerlist/brewery/add/
    url(r'brewery/add/$', views.BreweryCreate.as_view(), name='brewery-add'),

    # /beerlist/brewery/2/
    url(r'brewery/(?P<pk>[0-9]+)/$', views.BreweryUpdate.as_view(), name='brewery-update'),

    # /beerlist/brewery/2/delete/
    url(r'brewery/(?P<pk>[0-9]+)/delete/$', views.BreweryDelete.as_view(), name='brewery-delete')
]
