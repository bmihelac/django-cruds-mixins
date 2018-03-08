from django import forms
from django.http import HttpResponseRedirect

from .navigation import (
    NavigationItem,
)


class BulkSelectionBaseForm(forms.Form):
    """
    Base form for bulk selection actions.
    """
    action = forms.CharField(widget=forms.HiddenInput)
    select_all = forms.NullBooleanField(widget=forms.HiddenInput)
    selection = forms.MultipleChoiceField(widget=forms.MultipleHiddenInput,
                                          required=False)

    def set_selection(self, selection):
        self.fields['selection'].choices = [(s, s) for s in selection]


class BulkActionsMixin(object):
    """
    Support for bulk actions via post method.

    ::

        bulk_actions - list of method names for bulk actions
    """
    bulk_actions = None

    def get_bulk_action_methods(self):
        if self.bulk_actions is None:
            return []
        return self.bulk_actions[:]

    def get_bulk_action_actions(self):
        """
        Creates bulk selection actions from ``bulk_actions``.
        """
        actions = []
        for action_name in self.get_bulk_action_methods():
            action = getattr(self, action_name)
            title = getattr(action, 'short_description', action_name)
            actions.append(NavigationItem(
                title=title,
                url=None,
                code=action_name,
                css_class='btn',
            ))
        return actions

    def get_bulk_selection(self):
        ids = self.request.POST.getlist('selection')
        return ids

    def get_export_queryset(self):
        return self.get_queryset()

    def get_bulk_queryset(self, select_all, selection):
        if select_all:
            return self.get_export_queryset()
        return self.get_export_queryset().filter(id__in=selection)

    def get_bulk_action_name(self):
        """
        """
        return self.request.POST.get('action')

    def get_bulk_action(self, action_name):
        if action_name not in self.get_bulk_action_methods():
            return None
        return getattr(self, action_name)

    def post(self, request, *args, **kwargs):
        form = BulkSelectionBaseForm(data=request.POST)
        selection = self.get_bulk_selection()
        form.set_selection(selection)
        assert form.is_valid()
        data = form.cleaned_data
        action = self.get_bulk_action(data['action'])
        queryset = self.get_bulk_queryset(data['select_all'], selection)
        resp = action(
            request=request,
            action_name=data['action'],
            selection=data['selection'],
            select_all=data['select_all'],
            queryset=queryset
        )
        return resp or HttpResponseRedirect(request.get_full_path())