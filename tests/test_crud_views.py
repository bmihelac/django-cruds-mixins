from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser
from snapshottest.django import TestCase

from cruds_mixins.views.crud import (
    CRUDListView,
)

from .testapp.models import Author
from . import test_helper


class BaseTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.author = test_helper.create_author()


class TestCRUDListView(BaseTestCase):

    def test_default(self):
        view = CRUDListView.as_view(model=Author)
        request = self.factory.get('')
        request.user = AnonymousUser
        response = view(request)
        response.render()
        # from .browser import display; display(response.content)
        self.assertMatchSnapshot(response.content)
