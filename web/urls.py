from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^artikel/$', views.artikel, name='artikel'),
    url(r'^berita/$', views.berita, name='berita'),
    url(r'^berita/view/(?P<id>[0-9]+)/$', views.berita_view, name='berita_view'),
    url(r'^artikel/view/(?P<id>[0-9]+)/$', views.artikel_view, name='artikel_view'),
]
