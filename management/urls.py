from django.conf.urls import url

from . import views

app_name = 'management'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create_new', views.create_new, name='create_new'),
    url(r'^delete/(?P<projectid>\d+)/$', views.delete_project, name='delete'),
]
