from django.shortcuts import (
    redirect,
)
from django.urls import NoReverseMatch
from django.contrib import messages
from django.utils.module_loading import import_string
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponseRedirect

from cruds import utils as cruds_utils
from ..conf import CrudsMixinsConf
from ..utils.text import create_model_title
from ..mixins.navigation import (
    NavigationItem,
)


class CRUDMixin(object):
    """Mixin that provides common functionalities for CRUD views.

        ``base_template``
        ``default_template_name``
        ``permission_class``
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
        return self.get_base_queryset()

    # actions
    def get_action(self, title, url, **kwargs):
        """Creates NavigationItem for given action.
        """
        data = {
            'title': title,
            'url': url,
            'css_class': CrudsMixinsConf.CSS_CLASS_BUTTON,
        }
        data.update(kwargs)
        return NavigationItem(**data)

    def get_create_action(self):
        if not self.can_create():
            return None
        try:
            return self.get_action(
                create_model_title(self.model),
                self.get_create_url(),
                css_class=CrudsMixinsConf.CSS_CLASS_BUTTON_PRIMARY,
            )
        except NoReverseMatch:
            return None

    def get_update_action(self):
        if not self.can_update():
            return None
        try:
            return self.get_action(
                _('edit'),
                self.get_update_url(self.object),
                css_class=CrudsMixinsConf.CSS_CLASS_BUTTON_PRIMARY,
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
                css_class=CrudsMixinsConf.CSS_CLASS_BUTTON_DANGER,
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
    def add_message_and_redirect(self, msg, url, msg_type=None, extra_tags=''):
        if not msg_type:
            msg_type = messages.INFO
        messages.add_message(self.request, msg_type, msg, extra_tags)
        return redirect(url)

    def add_error_message_and_redirect(self, msg, url):
        return self.add_message_and_redirect(msg, url, messages.ERROR, 'danger')

    # form handling
    def get_message(self):
        """Returns msg, msg_type tuple or None if no message should be added.

        :returns: (msg, msg_type)
        """
        raise NotImplementedError

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
