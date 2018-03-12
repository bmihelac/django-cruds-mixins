# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponseRedirect
from django.views.generic import (
    ListView,
    TemplateView,
)
from django.contrib import messages

from django_tables2 import RequestConfig
from ..tables.tables import table_factory
from .bulk_actions import BulkActionsMixin


DEFAULT_SKIP_FIELDS = ['id', 'created', 'modified', 'created_by', 'updated_by']


class TableView(BulkActionsMixin, ListView):
    """
    Mixin adds a table with current queryset to context.


    ::
        table - django_tables2 table

        per_page
    """
    table = None
    table_fields = None
    table_exclude_fields = None
    per_page = 25

    def get_table_fields(self):
        if self.table_fields:
            return self.table_fields
        exclude = DEFAULT_SKIP_FIELDS + (self.table_exclude_fields or [])
        return [field.name for field in self.model._meta.fields
                if field.name not in exclude]

    def get_table_class(self):
        if self.table:
            return self.table
        fields = self.get_table_fields()
        return table_factory(self.model, fields)

    def get_table(self, *args, **kwargs):
        return self.get_table_class()(*args, **kwargs)

    def get_bulk_action_url(self):
        """
        Deprecated.

        Leave empty for inline bulk selection.
        """
        return None

    def annotate_table_queryset(self, qs):
        """
        Hook method allows annotating paginated and sorted queryset.
        """
        pass

    def get_context_data(self, *args, **kwargs):
        ctx = super(TableView, self).get_context_data(*args, **kwargs)
        queryset = ctx['object_list']
        table = self.get_table(queryset)
        RequestConfig(self.request, {'per_page': self.per_page}).configure(table)
        self.annotate_table_queryset(table.page.object_list.data)
        ctx['table'] = table
        ctx['bulk_action_url'] = self.get_bulk_action_url()
        ctx['bulk_action_actions'] = self.get_bulk_action_actions()
        return ctx


class BulkSelectionView(TemplateView):
    """
    View that display intermediate page with form and process selection on
    form valid.
    """
    template_name = 'cruds_mixins/bulk_selection_form.html'
    form_class = None

    def add_message(self, msg):
        """
        Adds a message.
        """
        messages.add_message(self.request, messages.INFO, msg)

    def get_form(self, action_name, selection, select_all):
        """
        Returns form.
        """
        kwargs = {
        }
        initial = {
            'action': action_name,
            'selection': selection,
            'select_all': select_all,
        }
        if 'submit' in self.request.POST:
            kwargs['data'] = self.request.POST
        form = self.form_class(initial=initial, **kwargs)
        form.fields['selection'].choices = [(s, s) for s in selection]
        return form

    def redirect(self):
        """
        Redirect to itself.
        """
        return HttpResponseRedirect(self.request.get_full_path())

    def post(self, request, action_name, selection, select_all, queryset, *args, **kwargs):
        form = self.get_form(action_name, selection, select_all)
        self.queryset = queryset
        if form.is_bound and form.is_valid():
            return self.form_valid(form)
        ctx = self.get_context_data(
            form=form, selection=selection, queryset=queryset,
            title=self.get_title(),
        )
        return self.render_to_response(ctx)
