from unittest import mock
from django.test import RequestFactory, override_settings
from django.contrib.auth.models import AnonymousUser
from django.test.testcases import TestCase
from django.views.generic import ListView, DetailView

from cruds_mixins import permission_classes
from cruds_mixins.mixins.cruds import (
    CRUDMixin,
)
from cruds_mixins.permission_classes import (
    AllowNoone,
)

from .testapp.models import Author
from .test_helper import (
    create_author,
)


class BaseTestCase(TestCase):
    def setUp(self):
        self.author = create_author()
        self.factory = RequestFactory()
        self.anonymous_user = AnonymousUser()
        self.request = self.factory.get('')
        self.request.user = self.anonymous_user


class CRUDMixinTestCase(BaseTestCase):

    def test_get_permissions_default(self):
        crud_mixin = CRUDMixin()
        permissions = crud_mixin.get_permissions()
        self.assertIsInstance(
            permissions,
            permission_classes.AllowAny
        )

    def test_get_permissions_custom(self):
        class MyView(CRUDMixin):
            permission_class = permission_classes.IsStaffOrReadOnly
        view = MyView()
        self.assertIsInstance(
            view.get_permissions(),
            permission_classes.IsStaffOrReadOnly
        )

    def test_get_urls(self):
        class MyView(CRUDMixin):
            model = Author

        view = MyView()
        view.get_list_url()
        view.get_create_url()
        view.get_update_url(self.author)
        view.get_detail_url(self.author)
        view.get_delete_url(self.author)

    def test_get_actions_without_permissions(self):
        class MyView(CRUDMixin, DetailView):
            model = Author
            permission_class = AllowNoone

            def get(self, request, *args, **kwargs):
                self.object = self.get_object()
                return [
                    self.get_update_action(),
                    self.get_delete_action(),
                    self.get_create_action(),
                ]

        result = MyView.as_view()(self.request, pk=self.author.pk)
        self.assertEqual(result, [None] * 3)

    @override_settings(ROOT_URLCONF=[])
    def test_get_actions_no_reverse_match(self):

        class MyView(CRUDMixin, DetailView):
            model = Author

            def get(self, request, *args, **kwargs):
                self.object = self.get_object()
                return [
                    self.get_update_action(),
                    self.get_delete_action(),
                    self.get_create_action(),
                ]

        result = MyView.as_view()(self.request, pk=self.author.pk)
        self.assertEqual(result, [None] * 3)

    def test_base_template(self):

        class MyView(CRUDMixin, ListView):
            model = Author
            base_template = 'test_base.html'

        view = MyView.as_view()
        response = view(self.factory.get(''))
        self.assertIn('base_template', response.context_data)

    @mock.patch('cruds_mixins.mixins.cruds.messages')
    def test_add_error_message_and_redirect(self, mock_module):

        class MyView(CRUDMixin, ListView):
            model = Author

            def get(self, request, *args, **kwargs):
                return self.add_error_message_and_redirect('error', '/')

        result = MyView.as_view()(self.request)
        self.assertTrue(mock_module.add_message.called)
        self.assertEqual(result.status_code, 302)
