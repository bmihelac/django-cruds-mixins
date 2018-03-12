from unittest.mock import patch
from datetime import date

from django.http import (
    HttpResponseRedirect,
    HttpResponseBadRequest,
)
from django.test import TestCase
from django.views.generic import ListView
from django.test import RequestFactory

from cruds_mixins.mixins.bulk_actions import (
    BulkActionsMixin,
)

from .testapp.models import Author


class MyView(BulkActionsMixin, ListView):
    model = Author
    bulk_actions = (
        'test_bulk_action',
    )

    def test_bulk_action(self, *args, **kwargs):
        pass


class BulkActionsMixinTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.view = MyView.as_view()
        self.author = Author.objects.create(
            name='Foo bar',
            birthday=date(2000, 1, 1),
        )
        self.author2 = Author.objects.create(
            name='fuu',
            birthday=date(2000, 1, 1),
        )

    def test_selection(self):
        with patch.object(MyView, 'test_bulk_action', return_value=None) as mock_method:
            response = self.view(self.factory.post('', data={
                'action': 'test_bulk_action',
                'selection': [self.author.pk]
            }))
            qs = mock_method.call_args[1]['queryset']
            self.assertIn(self.author, qs)
            self.assertNotIn(self.author2, qs)
            self.assertIsInstance(response, HttpResponseRedirect)

    def test_non_existing_action(self):
        response = self.view(self.factory.post('', data={
            'action': 'non_existing',
        }))
        self.assertIsInstance(response, HttpResponseBadRequest)
