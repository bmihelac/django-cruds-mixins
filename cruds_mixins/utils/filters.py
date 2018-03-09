# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django_filters


class DefaultFilterSet(django_filters.FilterSet):
    pass


def filterset_factory(model, fields):
    meta = type('Meta',
                (object,), {
                    'model': model,
                    'fields': fields,
                })
    filterset = type(str('%sFilterSet' % model._meta.object_name),
                     (DefaultFilterSet,), {'Meta': meta})
    return filterset
