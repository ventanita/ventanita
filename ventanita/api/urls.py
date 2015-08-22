# Copyright 2015 by AniversarioPeru. All rights reserved.
# This code is part of the Ventanita distribution and governed by its
# license. Please see the LICENSE file that should have been included
# as part of this package.

from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    '',
    url(r'^proyecto.json/(?P<codigo>[0-9]+\-[0-9]+)/$', views.index),
)
