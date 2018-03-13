from django.test import RequestFactory
from snapshottest.django import TestCase

from cruds_mixins.mixins.tables import (
    TableView
)

from .testapp.models import Author
from .testapp.tables import AuthorTable
from . import test_helper


class TablesTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.author = test_helper.create_author()

    def test_default(self):
        request = self.factory.get('')
        view = TableView.as_view(
            model=Author,
            template_name='testapp/table.html'
        )
        response = view(request)
        self.assertEqual(response.status_code, 200)
        response.render()
        # from .browser import display; display(response.content)
        self.assertMatchSnapshot(response.content)

    def test_custom_table(self):
        request = self.factory.get('')
        view = TableView.as_view(
            model=Author,
            template_name='testapp/table.html',
            table=AuthorTable
        )
        response = view(request)
        self.assertEqual(response.status_code, 200)
        response.render()
        # from .browser import display; display(response.content)
        self.assertMatchSnapshot(response.content)
