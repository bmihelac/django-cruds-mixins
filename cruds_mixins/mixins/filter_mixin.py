# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..conf import CrudsMixinsConf
from ..utils.filters import filterset_factory
from ..utils.pagination import pagination_getvars


class FilterMixin(object):
    """

        ``filterset`` - FilterSet class. Leave empty to create FilterSet
        dynamically.  If ``filterset`` is ``None`` filterset will not be
        created.
    """
    filterset = None
    filterset_fields = None
    filterset_exclude_fields = None

    def get_filter_kwargs(self):
        return {}

    def get_filterset_fields(self):
        if self.filterset_fields:
            return self.filterset_fields
        exclude = CrudsMixinsConf.DEFAULT_SKIP_FIELDS + (self.filterset_exclude_fields or [])
        return [field.name for field in self.model._meta.fields
                if field.name not in exclude]

    def get_filterset(self):
        if self.filterset is False:
            return None
        if self.filterset:
            return self.filterset
        filterset = filterset_factory(self.model, self.get_filterset_fields())
        return filterset

    def get_filter(self, queryset):
        filterset = self.get_filterset()
        if filterset is None:
            return None
        filter_kwargs = self.get_filter_kwargs()
        data = self.request.GET or None
        return filterset(
            data=data,
            queryset=queryset,
            **filter_kwargs
        )

    def get_filtered_queryset(self, queryset):
        self.filter = self.get_filter(queryset)
        if self.filter is None:
            return queryset
        return self.filter.qs

    def get_queryset(self):
        qs = super(FilterMixin, self).get_queryset()
        return self.get_filtered_queryset(qs)

    def get_context_data(self, **kwargs):
        ctx = super(FilterMixin, self).get_context_data(**kwargs)
        if hasattr(self, 'filter'):
            ctx['filter'] = self.filter
            ctx['getvars'] = pagination_getvars(
                self.request.META['QUERY_STRING'])
        return ctx
