# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import (
    redirect,
)
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse, NoReverseMatch
from django.http import HttpResponseRedirect
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from rules.contrib.views import PermissionRequiredMixin

from cruds import utils as cruds_utils
from ..utils.text import create_model_title
from ..mixins.navigation import (
    ActionsMixin,
    NavigationItem,
)
from ..mixins.tables import TableView
from ..mixins.filter_mixin import FilterMixin


class CRUDPermissionRequiredMixin(PermissionRequiredMixin):
    raise_exception = True

    def get_permission_required(self):
        raise NotImplementedError

    def can_create(self):
        return self.request.user.has_perm(
            cruds_utils.crud_permission_name(self.model, cruds_utils.ACTION_CREATE),
            self.get_object(),
        )


class CRUDMixin(object):
    """
    Define `for_user` manager method for model.
    Define rules app_model_action
    """
    base_template = None
    default_template_name = None

    # permissions
    def can_list(self):
        return True

    def can_create(self):
        return True

    def can_update(self):
        return True

    def can_detail(self):
        return True

    def can_delete(self):
        return True

    # urls
    def get_list_url(self):
        return cruds_utils.crud_url(self.model, cruds_utils.ACTION_LIST)

    def get_create_url(self):
        return cruds_utils.crud_url(self.model, cruds_utils.ACTION_CREATE)

    def get_update_url(self):
        return cruds_utils.crud_url(self.model, cruds_utils.ACTION_UPDATE)

    def get_detail_url(self):
        return cruds_utils.crud_url(self.model, cruds_utils.ACTION_DETAIL)

    def get_delete_url(self):
        return cruds_utils.crud_url(self.model, cruds_utils.ACTION_DELETE)

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
                self.get_edit_url()
            )
        except NoReverseMatch:
            return None

    def get_delete_action(self):
        if not self.can_delete():
            return None
        try:
            return self.get_action(
                _('edit'),
                self.get_delete_url(),
                css_class='btn btn-danger',
            )
        except NoReverseMatch:
            return None

    # templates
    def get_base_template(self):
        return self.base_template

    def get_template_names(self):
        template_names = super(CRUDMixin, self).get_template_names()
        if hasattr(self, 'default_template_name'):
            template_names.append(self.default_template_name)
        return template_names

    def get_title(self):
        if isinstance(self, TableView):
            return self.model._meta.verbose_name_plural.capitalize()
        elif isinstance(self, CreateView):
            return create_model_title(self.model)
        elif isinstance(self, DeleteView):
            return _('Delete %(model)s: %(object)s') % {
                'model': unicode(self.object._meta.verbose_name),
                'object': unicode(self.object),
            }
        elif isinstance(self, UpdateView):
            return _('Edit %(object)s') % {'object': unicode(self.object)}
        elif isinstance(self, DetailView):
            return unicode(self.object)
        return ""

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


class CRUDListView(CRUDMixin,
                   ActionsMixin, FilterMixin, TableView):
    default_template_name = 'cruds_mixins/list.html'

    def get_actions(self):
        return [self.get_create_action()]

    def test_func(self, user):
        return self.test_func_list(user)

    def get_summary(self):
        """
        Returns summary of objects by field `status`.
        """
        qs = self.get_base_queryset()
        summary = []
        for key, name in self.model._meta.get_field_by_name('status')[0].choices:
            summary.append((key, name, qs.filter(status=key).count()))
        return summary


class CRUDDetailView(CRUDMixin,
                     ActionsMixin, DetailView):
    default_template_name = 'cruds_mixins/detail.html'

    def get_actions(self):
        return [self.get_update_action()]

    def test_func(self, user):
        return self.test_func_detail(user)


class CRUDCreateView(CRUDMixin, CreateView):
    default_template_name = 'cruds_mixins/form.html'
    add_message = False

    def get_message(self):
        if not self.add_message:
            return None
        return (_('Object %s has been created') % self.object, messages.INFO)

    def test_func(self, user):
        return self.test_func_create(user)


class CRUDUpdateView(CRUDMixin, ActionsMixin, UpdateView):
    default_template_name = 'cruds_mixins/form.html'
    add_message = False

    def get_message(self):
        if not self.add_message:
            return None
        return (_('Object %s has been updated') % self.object, messages.INFO)

    def test_func(self, user):
        return self.test_func_update(user)

    def get_actions(self):
        return [self.get_delete_action()]


class CRUDDeleteView(CRUDMixin, DeleteView):
    default_template_name = 'cruds_mixins/delete.html'

    def test_func(self, user):
        return self.test_func_delete(user)

    def get_success_url(self):
        return reverse(cruds_utils.crud_url_name(self.model, 'list'))

    def delete(self, request, *args, **kwargs):
        resp = super(CRUDDeleteView, self).delete(request, *args, **kwargs)
        msg = _('Record has been deleted.')
        messages.add_message(request, messages.INFO, msg)
        return resp
