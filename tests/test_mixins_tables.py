from django.test import RequestFactory
from snapshottest.django import TestCase

from django_tables2 import Table
from cruds_mixins.mixins.tables import (
    TableView
)

from .testapp.models import Author
from .testapp.tables import AuthorTable
from . import test_helper


class TablesTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.request = self.factory.get('')
        self.author = test_helper.create_author()

    def test_default(self):
        view = TableView.as_view(
            model=Author,
            template_name='testapp/table.html'
        )
        response = view(self.request)
        self.assertEqual(response.status_code, 200)
        response.render()
        # from .browser import display; display(response.content)
        self.assertMatchSnapshot(test_helper.semantic_html(response.content))

    def test_custom_table(self):
        view = TableView.as_view(
            model=Author,
            template_name='testapp/table.html',
            table=AuthorTable
        )
        response = view(self.request)
        self.assertEqual(response.status_code, 200)
        response.render()
        # from .browser import display; display(response.content)
        self.assertMatchSnapshot(test_helper.semantic_html(response.content))

    def test_with_table_fields(self):
        view = TableView.as_view(
            model=Author,
            template_name='testapp/table.html',
            table_fields=('name',)
        )
        response = view(self.request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'name')
        self.assertNotContains(response, 'birthday')
