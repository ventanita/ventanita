# Copyright 2015 by AniversarioPeru. All rights reserved.
# This code is part of the Ventanita distribution and governed by its
# license. Please see the LICENSE file that should have been included
# as part of this package.

from django.conf.urls import patterns, include, url
from core.views import index

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),
    url(r'^demo/$', include('demo.urls', namespace='demo')),
    url(r'^entidades/$', 'pages.views.entidades', name='entidades'),
)
