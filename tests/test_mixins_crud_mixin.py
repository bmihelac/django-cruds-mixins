from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.test.testcases import TestCase
from django.views.generic.detail import SingleObjectMixin

from cruds_mixins import permission_classes
from cruds_mixins.views.crud import CRUDMixin
from cruds_mixins.permission_classes import (
    AllowNoone,
)

from .testapp.models import Author
from .test_helper import (
    create_author,
)


class CRUDMixinTestCase(TestCase):

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
        instance = create_author()

        class MyView(CRUDMixin):
            model = Author

        view = MyView()
        view.get_list_url()
        view.get_create_url()
        view.get_update_url(instance)
        view.get_detail_url(instance)
        view.get_delete_url(instance)

    def test_get_actions_without_permissions(self):
        request = RequestFactory().get('')
        request.user = AnonymousUser

        class MyView(CRUDMixin, SingleObjectMixin):
            model = Author
            permission_class = AllowNoone

        view = MyView()
        view.request = request
        view.kwargs = {
            'pk': create_author().pk,
        }
        self.assertIsNone(view.get_update_action())
        self.assertIsNone(view.get_delete_action())
        self.assertIsNone(view.get_create_action())
