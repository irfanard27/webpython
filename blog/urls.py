from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^artikel/count/$', views.ajax_artikel_count, name='count_artikel'),
    url(r'^artikel/all/$', views.ajax_artikel_all, name='all_artikel'),
]
