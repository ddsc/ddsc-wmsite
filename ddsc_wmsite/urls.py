# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from django.contrib import admin
from lizard_ui.urls import debugmode_urlpatterns

from ddsc_wmsite import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^ui/', include('lizard_ui.urls')),
    # url(r'^map/', include('lizard_map.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^wms/', views.showshow, name="showshow"),
    # url(r'^something_else/$',
    #     views.SomeClassBasedView.as_view(),
    #     name='name_it_too'),
    )
urlpatterns += debugmode_urlpatterns()
