# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from cruds_mixins.urls import urlpatterns as cruds_mixins_urls

urlpatterns = [
    url(r'^', include(cruds_mixins_urls)),
]
