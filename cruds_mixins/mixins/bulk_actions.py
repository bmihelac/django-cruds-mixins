from django import forms
from django.http import (
    HttpResponseRedirect,
    HttpResponseBadRequest,
    HttpResponseForbidden,
)
from django.views.generic import (
    TemplateView,
)
from django.views.generic.edit import (
    FormMixin,
)

from cruds import utils as cruds_utils
from ..conf import CrudsMixinsConf
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
    """Mixin adds support for bulk actions via post method.

        ``bulk_actions`` - list of method names for bulk actions. Each action
        method can define `short_description` that would be used as a label.
    """
    bulk_actions = None

    def get_bulk_action_name(self):
        return self.request.POST['action']

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
                css_class=CrudsMixinsConf.CSS_CLASS_BUTTON,
            ))
        return actions

    def get_bulk_selection(self):
        ids = self.request.POST.getlist('selection')
        return ids

    def get_bulk_queryset(self, select_all, selection):
        if select_all:
            return self.get_queryset()
        return self.get_queryset().filter(id__in=selection)

    def get_bulk_action(self, action_name):
        if action_name not in self.get_bulk_action_methods():
            return None
        return getattr(self, action_name)

    def can_bulk_action(self):
        return True

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx['bulk_action_actions'] = self.get_bulk_action_actions()
        return ctx

    def post(self, request, *args, **kwargs):
        if not self.can_bulk_action():
            return HttpResponseForbidden('forbidden')
        form = BulkSelectionBaseForm(data=request.POST)
        selection = self.get_bulk_selection()
        form.set_selection(selection)
        assert form.is_valid()
        data = form.cleaned_data
        action_name = self.get_bulk_action_name()
        action = self.get_bulk_action(action_name)
        if action is None:
            return HttpResponseBadRequest('invalid action')
        queryset = self.get_bulk_queryset(data['select_all'], selection)
        resp = action(
            request=request,
            action_name=data['action'],
            selection=data['selection'],
            select_all=data['select_all'],
            queryset=queryset
        )
        return resp or HttpResponseRedirect(request.get_full_path())


class BulkSelectionActionBaseView(FormMixin, TemplateView):
    """Base intermediate view for processing bulk actions.
    """
    template_name = 'cruds_mixins/bulk_selection_form.html'
    form_class = BulkSelectionBaseForm

    def get_initial(self):
        initial = super().get_initial()
        initial = {
            'action': self.action_name,
            'selection': self.selection,
            'select_all': self.select_all,
        }
        return initial

    def get_form_kwargs(self):
        kwargs = {
            'initial': self.get_initial(),
            'prefix': self.get_prefix(),
        }

        if 'submit' in self.request.POST:
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        return kwargs

    def get_success_url(self):
        return cruds_utils.crud_url(self.queryset.model, cruds_utils.ACTION_LIST)

    def post(self, request, action_name, selection, select_all, queryset, *args, **kwargs):
        self.action_name = action_name
        self.selection = selection
        self.select_all = select_all
        self.queryset = queryset

        form = self.get_form()

        if form.is_bound and form.is_valid():
            return self.form_valid(form)
        ctx = self.get_context_data(
            form=form, selection=selection, queryset=queryset,
            title=self.get_title(),
        )
        return self.render_to_response(ctx)
