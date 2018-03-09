from datetime import date

from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from snapshottest.django import TestCase

from cruds_mixins.views.crud import (
    CRUDListView,
)

from .testapp.models import Author


class BaseTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.author = Author.objects.create(
            name='Foo bar',
            birthday=date(2000, 1, 1),
        )


class TestCRUDListView(BaseTestCase):

    def test_default(self):
        view = CRUDListView.as_view(model=Author)
        request = self.factory.get('')
        request.user = AnonymousUser
        response = view(request)
        response.render()
        from .browser import display; display(response.content)
        # self.assertMatchSnapshot(response.content)
