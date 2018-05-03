from unittest import mock

from django.test.html import parse_html
from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser
from snapshottest.django import TestCase

from cruds_mixins.views.crud import (
    CRUDListView,
    CRUDUpdateView,
)

from .testapp.models import Author
from . import test_helper


class BaseTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.author = test_helper.create_author()
        self.anonymous_user = AnonymousUser()


class TestCRUDListView(BaseTestCase):

    def test_default(self):
        view = CRUDListView.as_view(model=Author)
        request = self.factory.get('')
        request.user = AnonymousUser
        response = view(request)
        response.render()
        # from .browser import display; display(response.content)
        self.assertMatchSnapshot(test_helper.semantic_html(response.content))


class CRUDUpdateViewTest(BaseTestCase):

    @mock.patch('cruds_mixins.mixins.cruds.messages')
    def test_without_message(self, mock_module):
        class MyView(CRUDUpdateView):
            model = Author
            fields = ('name', )

            def get_message(self):
                return None

        self.request = self.factory.post('', {
            'name': 'aaa'
        })
        self.request.user = self.anonymous_user
        MyView.as_view()(self.request, pk=self.author.pk)
        self.assertFalse(mock_module.add_message.called)
