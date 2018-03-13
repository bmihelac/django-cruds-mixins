from django.shortcuts import (
    redirect,
)
from django.contrib import messages
from django.utils.module_loading import import_string
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse, NoReverseMatch
from django.http import HttpResponseRedirect
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import UserPassesTestMixin

from cruds import utils as cruds_utils
from ..conf import CrudsMixinsConf
from ..utils.text import create_model_title
from ..mixins.navigation import (
    ActionsMixin,
    NavigationItem,
)
from ..mixins.tables import TableView
from ..mixins.filter_mixin import FilterMixin


class CRUDMixin(object):
    """
    Define `for_user` manager method for model.
    Define rules app_model_action
    """
    base_template = None
    default_template_name = None
    permission_class = None
    _permissions = None

    # permissions
    def get_permissions(self):
        if self._permissions:
            return self._permissions
        if self.permission_class:
            self._permissions = self.permission_class()
        else:
            self._permissions = import_string(
                CrudsMixinsConf.DEFAULT_PERMISSION_CLASS)()
        return self._permissions

    def can_list(self):
        return self.get_permissions().can_list(
            self.request.user,
            self.model,
            self
        )

    def can_create(self):
        return self.get_permissions().can_create(
            self.request.user,
            self.model,
            self
        )

    def can_update(self):
        return self.get_permissions().can_update(
            self.request.user,
            self.model,
            self.get_object(),
            self
        )

    def can_detail(self):
        return self.get_permissions().can_detail(
            self.request.user,
            self.model,
            self.get_object(),
            self
        )

    def can_delete(self):
        return self.get_permissions().can_delete(
            self.request.user,
            self.model,
            self.get_object(),
            self
        )

    # urls
    def get_list_url(self):
        return cruds_utils.crud_url(self.model, cruds_utils.ACTION_LIST)

    def get_create_url(self):
        return cruds_utils.crud_url(self.model, cruds_utils.ACTION_CREATE)

    def get_update_url(self, instance):
        return cruds_utils.crud_url(instance, cruds_utils.ACTION_UPDATE)

    def get_detail_url(self, instance):
        return cruds_utils.crud_url(instance, cruds_utils.ACTION_DETAIL)

    def get_delete_url(self, instance):
        return cruds_utils.crud_url(instance, cruds_utils.ACTION_DELETE)

    # queryset
    def get_base_queryset(self):
        """Allows subclasses to hook.
        """
        if hasattr(self.model.objects, 'for_user'):
            queryset = self.model.objects.for_user(self.request.user)
        else:
            queryset = super(CRUDMixin, self).get_queryset()
        return queryset

    def get_queryset(self):
        queryset = self.get_base_queryset()
        if hasattr(self, 'get_filtered_queryset'):
            queryset = self.get_filtered_queryset(queryset)
        return queryset

    # actions
    def get_action(self, title, url, **kwargs):
        """Creates NavigationItem for given action.
        """
        data = {
            'title': title,
            'url': url,
            'css_class': 'btn btn-default',
        }
        data.update(kwargs)
        return NavigationItem(**data)

    def get_create_action(self):
        if not self.can_create():
            return None
        try:
            return self.get_action(
                create_model_title(self.model),
                self.get_create_url()
            )
        except NoReverseMatch:
            return None

    def get_update_action(self):
        if not self.can_update():
            return None
        try:
            return self.get_action(
                _('edit'),
                self.get_update_url(self.object)
            )
        except NoReverseMatch:
            return None

    def get_delete_action(self):
        if not self.can_delete():
            return None
        try:
            return self.get_action(
                _('delete'),
                self.get_delete_url(self.object),
                css_class='btn btn-danger',
            )
        except NoReverseMatch:
            return None

    # templates
    def get_base_template(self):
        return self.base_template

    def get_template_names(self):
        template_names = super(CRUDMixin, self).get_template_names()
        if self.default_template_name:
            template_names.append(self.default_template_name)
        return template_names

    def get_title(self):
        return self.model._meta.verbose_name_plural.capitalize()

    def get_context_data(self, **kwargs):
        context = super(CRUDMixin, self).get_context_data(**kwargs)
        context['title'] = self.get_title()
        base_template = self.get_base_template()
        if base_template:
            context['base_template'] = base_template
        return context

    # misc
    def update_instance(self, instance):
        """
        Hook allows updating instance before saving.
        """

    # messages
    def get_message(self):
        """Returns msg, msg_type tuple or None if no message should be added.

        :returns: (msg, msg_type)
        """
        return None

    def add_message_and_redirect(self, msg, url, msg_type=None, extra_tags=''):
        if not msg_type:
            msg_type = messages.INFO
        messages.add_message(self.request, msg_type, msg, extra_tags)
        return redirect(url)

    def add_error_message_and_redirect(self, msg, url):
        return self.add_message_and_redirect(msg, url, messages.ERROR, 'danger')

    # form handling
    def form_valid(self, form):
        """
        Calls ``update_instance``, adds message if defined.
        """
        self.object = form.save(commit=False)
        self.update_instance(self.object)
        self.object.save()
        form.save_m2m()
        message = self.get_message()
        if message:
            messages.add_message(self.request, message[1], message[0])
        return HttpResponseRedirect(self.get_success_url())

    # urls
    def get_next_url(self):
        """
        Return `next` from GET or POST parameter or None.
        """
        return self.request.GET.get(
            'next',
            self.request.POST.get(
                'next',
                None
            )
        )

    def get_success_url(self):
        return self.get_next_url() or super(CRUDMixin, self).get_success_url()


class CRUDListView(CRUDMixin, UserPassesTestMixin,
                   ActionsMixin, FilterMixin, TableView):
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
    add_message = True

    def test_func(self):
        return self.can_create()

    def get_title(self):
        return create_model_title(self.model)

    def get_message(self):
        if not self.add_message:
            return None
        return (_('Object %s has been created') % self.object, messages.INFO)


class CRUDUpdateView(CRUDMixin, UserPassesTestMixin, ActionsMixin, UpdateView):
    default_template_name = 'cruds_mixins/form.html'
    add_message = True

    def test_func(self):
        return self.can_update()

    def get_title(self):
        return _('Edit %(object)s') % {'object': str(self.object)}

    def get_message(self):
        if not self.add_message:
            return None
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
        return reverse(cruds_utils.crud_url_name(self.model, 'list'))

    def delete(self, request, *args, **kwargs):
        resp = super(CRUDDeleteView, self).delete(request, *args, **kwargs)
        msg = _('Record has been deleted.')
        messages.add_message(request, messages.INFO, msg)
        return resp
