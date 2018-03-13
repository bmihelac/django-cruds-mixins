from django.test.testcases import TestCase
from django.contrib.auth.models import AnonymousUser, User

import rules
from cruds_mixins import permission_classes
from cruds_mixins.utils.rules import add_crud_perms
from .testapp.models import Author
from .test_helper import (
    create_author,
    reset_ruleset,
)


class BaseTestCase(TestCase):

    def setUp(self):
        self.anonymous_user = AnonymousUser()
        self.permissions = self.get_permissions()
        self.author = create_author()

    def get_permissions(self):
        raise NotImplementedError


class AllowAnyTest(BaseTestCase):

    def get_permissions(self):
        return permission_classes.AllowAny()

    def test_can_list(self):
        self.assertTrue(self.permissions.can_list(
            self.anonymous_user,
            Author
        ))

    def test_can_create(self):
        self.assertTrue(self.permissions.can_create(
            self.anonymous_user,
            Author
        ))

    def test_can_update(self):
        self.assertTrue(self.permissions.can_update(
            self.anonymous_user,
            Author,
            self.author
        ))

    def test_can_detail(self):
        self.assertTrue(self.permissions.can_detail(
            self.anonymous_user,
            Author,
            self.author
        ))

    def test_can_delete(self):
        self.assertTrue(self.permissions.can_delete(
            self.anonymous_user,
            Author,
            self.author
        ))


class IsStaffOrReadOnlyTest(BaseTestCase):

    def setUp(self):
        super(IsStaffOrReadOnlyTest, self).setUp()
        self.user = User.objects.create_user('staff', is_staff=True)

    def get_permissions(self):
        return permission_classes.IsStaffOrReadOnly()

    def test_can_list(self):
        self.assertTrue(self.permissions.can_list(
            self.anonymous_user,
            Author
        ))
        self.assertTrue(self.permissions.can_list(
            self.user,
            Author
        ))

    def test_can_create(self):
        self.assertFalse(self.permissions.can_create(
            self.anonymous_user,
            Author
        ))
        self.assertTrue(self.permissions.can_create(
            self.user,
            Author
        ))

    def test_can_update(self):
        self.assertFalse(self.permissions.can_update(
            self.anonymous_user,
            Author,
            self.author
        ))
        self.assertTrue(self.permissions.can_update(
            self.user,
            Author,
            self.author
        ))

    def test_can_detail(self):
        self.assertTrue(self.permissions.can_detail(
            self.anonymous_user,
            Author,
            self.author
        ))
        self.assertTrue(self.permissions.can_detail(
            self.user,
            Author,
            self.author
        ))

    def test_can_delete(self):
        self.assertFalse(self.permissions.can_delete(
            self.anonymous_user,
            Author,
            self.author
        ))
        self.assertTrue(self.permissions.can_delete(
            self.user,
            Author,
            self.author
        ))


class RulesPermissionsTest(BaseTestCase):

    def setUp(self):
        super(RulesPermissionsTest, self).setUp()
        reset_ruleset()
        add_crud_perms(
            Author,
            list_predicate=rules.always_allow,
            create_predicate=rules.always_allow,
            update_predicate=rules.always_allow,
            detail_predicate=rules.always_allow,
            delete_predicate=rules.always_allow,
        )

    def get_permissions(self):
        return permission_classes.RulesPermissions()

    def test_can_list(self):
        self.assertTrue(self.permissions.can_list(
            self.anonymous_user,
            Author
        ))

    def test_can_create(self):
        self.assertTrue(self.permissions.can_create(
            self.anonymous_user,
            Author
        ))

    def test_can_update(self):
        self.assertTrue(self.permissions.can_update(
            self.anonymous_user,
            Author,
            self.author
        ))

    def test_can_detail(self):
        self.assertTrue(self.permissions.can_detail(
            self.anonymous_user,
            Author,
            self.author
        ))

    def test_can_delete(self):
        self.assertTrue(self.permissions.can_delete(
            self.anonymous_user,
            Author,
            self.author
        ))
