# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import django_filters


class DefaultFilterSet(django_filters.FilterSet):

    class Meta:
        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                }
            },
        }


def filterset_factory(model, fields):
    meta = type(
        'Meta',
        (DefaultFilterSet.Meta,),
        {'model': model, 'fields': fields}
    )
    filterset = type(
        '%sFilterSet' % model._meta.object_name,
        (DefaultFilterSet,),
        {'Meta': meta}
    )
    return filterset
