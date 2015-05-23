from django.conf.urls import patterns
from django.conf.urls import url

from . import views


urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    # url(r'^browse/$', views.browse, name='browse'),
)
