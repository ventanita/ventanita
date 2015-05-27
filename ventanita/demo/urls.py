# Copyright 2015 by AniversarioPeru. All rights reserved.
# Revisions 2015 copyright by RoxyRocker. All rights reserved.
# This code is part of the Ventanita distribution and governed by its
# license. Please see the LICENSE file that should have been included
# as part of this package.

from django.conf.urls import patterns
from django.conf.urls import url

from . import views


urlpatterns = patterns(
    '',
    url(r'^1400_candidatos/$', views.candidatos_con_sentencias, name='candidatos_con_sentencias'),
    url(r'^20_agrupaciones/$', views.las_20_agrupaciones, name='las_20_agrupaciones'),
    url(r'^sentenciados_homicidio/$', views.sentenciados_homicidio, name='sentenciados_homicidio'),
    url(r'^sentenciados_tid/$', views.sentenciados_tid, name='sentenciados_tid'),
    url(r'^$', views.index, name='index'),
    # url(r'^browse/$', views.browse, name='browse'),
)
