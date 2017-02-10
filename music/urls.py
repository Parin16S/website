from django.conf.urls import url
from django.conf.urls.i18n import urlpatterns

app_name = 'music'

from . import views #. mean the current directory

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    #music/album/add
    url(r'album/add/$', views.AlbumCreate.as_view(), name='albumadd'),
    #music/ ^ indicates the starting of the regular expression
    #url(r'^$', views.index , name='index'), # '$' symbol indicates the end i.e. if there in nothing after $ '/' in url(here after music/ nothing is there)
    #/music/<album_id>/
    #url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'), #^ represent beginning and $ represents end, album_id is the variable which can be used
    #name = 'detail' mean the above url pattern is recognized by detail
    #/music/<album_id>/favorite/
    #url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite')#we no longer need this after creating generic views

]

