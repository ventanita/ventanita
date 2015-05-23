from django.conf.urls import patterns
from django.conf.urls import url

from . import views


urlpatterns = patterns(
    '',
    url(r'^1400_candidatos/$', views.candidatos_con_sentencias, name='candidatos_con_sentencias'),
    url(r'^$', views.index, name='index'),
    # url(r'^browse/$', views.browse, name='browse'),
)
