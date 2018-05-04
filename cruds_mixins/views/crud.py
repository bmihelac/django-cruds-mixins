from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import UserPassesTestMixin as UserPassesTestMixinBase

from ..utils.text import create_model_title
from ..mixins.navigation import (
    ActionsMixin,
)
from ..mixins.tables import TableView
from ..mixins.filter_mixin import FilterMixin
from ..mixins.cruds import CRUDMixin


class UserPassesTestMixin(UserPassesTestMixinBase):
    raise_exception = True


class CRUDListView(FilterMixin, CRUDMixin, UserPassesTestMixin,
                   ActionsMixin, TableView):
    default_template_name = 'cruds_mixins/list.html'

    def test_func(self):
        return self.can_list()

    def get_actions(self):
        return [self.get_create_action()]


class CRUDDetailView(CRUDMixin, UserPassesTestMixin,
                     ActionsMixin, DetailView):
    default_template_name = 'cruds_mixins/detail.html'

    def test_func(self):
        return self.can_detail()

    def get_title(self):
        return str(self.object)

    def get_actions(self):
        return [self.get_update_action()]


class CRUDCreateView(CRUDMixin, UserPassesTestMixin, CreateView):
    default_template_name = 'cruds_mixins/form.html'

    def test_func(self):
        return self.can_create()

    def get_title(self):
        return create_model_title(self.model)

    def get_message(self):
        return (_('Object %s has been created') % self.object, messages.INFO)


class CRUDUpdateView(CRUDMixin, UserPassesTestMixin, ActionsMixin, UpdateView):
    default_template_name = 'cruds_mixins/form.html'

    def test_func(self):
        return self.can_update()

    def get_title(self):
        return _('Edit %(object)s') % {'object': str(self.object)}

    def get_message(self):
        return (_('Object %s has been updated') % self.object, messages.INFO)

    def get_actions(self):
        return [self.get_delete_action()]


class CRUDDeleteView(CRUDMixin, UserPassesTestMixin, DeleteView):
    default_template_name = 'cruds_mixins/delete.html'

    def test_func(self):
        return self.can_delete()

    def get_title(self):
        return _('Delete %(model)s: %(object)s') % {
            'model': str(self.object._meta.verbose_name),
            'object': str(self.object),
        }

    def get_success_url(self):
        return self.get_list_url()

    def delete(self, request, *args, **kwargs):
        resp = super(CRUDDeleteView, self).delete(request, *args, **kwargs)
        msg = _('Record has been deleted.')
        messages.add_message(request, messages.INFO, msg)
        return resp
