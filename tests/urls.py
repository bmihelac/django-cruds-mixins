# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import include

from .testapp import urls as testapp_urls
from django.urls import path


urlpatterns = [
    path('', include(testapp_urls)),
]
