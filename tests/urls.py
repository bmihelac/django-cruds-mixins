# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from .testapp import urls as testapp_urls


urlpatterns = [
    url(r'^', include(testapp_urls)),
]
