from django.test.testcases import TestCase

from cruds_mixins import permission_classes
from cruds_mixins.views.crud import CRUDMixin


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
