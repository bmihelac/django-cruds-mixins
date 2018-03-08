from django.test import TestCase, RequestFactory

from cruds_mixins.mixins.tables import (
    TableView
)

from .testapp.models import Author


class TablesTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_default(self):
        request = self.factory.get('')
        view = TableView.as_view(
            model=Author,
            template_name='testapp/table.html'
        )
        response = view(request)
        self.assertEqual(response.status_code, 200)
