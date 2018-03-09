from django.test import TestCase

from datetime import date

import django_tables2 as tables
from cruds_mixins.tables import columns

from .testapp.models import Author


class ViewLinkColumnTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create(
            name='foo',
            birthday=date.today(),
        )

    def test_default(self):

        class Table(tables.Table):
            view_link = columns.ViewLinkColumn()

        table = Table(Author.objects.all())
        self.assertEqual(
            table.rows[0].get_cell('view_link'),
            '<a href="/author/%d/">View</a>' % self.author.pk
        )
