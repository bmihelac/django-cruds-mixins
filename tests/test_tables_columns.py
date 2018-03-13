from django.test import TestCase

from datetime import date

import django_tables2 as tables
from cruds_mixins.tables import columns
from cruds import utils as cruds_utils

from .testapp.models import (
    Author,
    Continent,
    Country,
)


class BaseTestCase(TestCase):

    def setUp(self):
        self.continent = Continent.objects.create(
            name='Foo continent',
        )
        self.country = Country.objects.create(
            name='Foo country',
            continent=self.continent,
        )
        self.author = Author.objects.create(
            name='foo',
            birthday=date.today(),
            country=self.country,
        )


class ViewLinkColumnTest(BaseTestCase):

    def get_table(self, column):
        class Table(tables.Table):
            view_link = column

        table = Table(Author.objects.all())
        return table

    def test_default(self):
        table = self.get_table(columns.ViewLinkColumn())
        self.assertEqual(
            table.rows[0].get_cell('view_link'),
            '<a href="/author/%d/">View</a>' % self.author.pk
        )

    def test_action_name(self):
        table = self.get_table(columns.ViewLinkColumn(
            action_name='edit',
            action=cruds_utils.ACTION_UPDATE,
            verbose_name='action',
        ))
        self.assertEqual(
            table.columns[0].verbose_name, 'action'
        )
        self.assertEqual(
            table.rows[0].get_cell('view_link'),
            '<a href="/author/%d/edit/">edit</a>' % self.author.pk
        )

    def test_with_accessor(self):
        self.get_table(columns.ViewLinkColumn(accessor='pk'))


class FKColumnTest(BaseTestCase):

    def test_default(self):

        class Table(tables.Table):
            class Meta:
                model = Author
                fields = (
                    'country',
                )

        table = Table(Author.objects.all())
        self.assertEqual(
            table.rows[0].get_cell('country'),
            '<a href="/country/%d/">%s</a>' % (
                self.country.pk,
                self.country.name,
            )
        )

    def test_without_link(self):
        class Table(tables.Table):
            class Meta:
                model = Country
                fields = (
                    'continent',
                )
        table = Table(Country.objects.all())
        self.assertEqual(
            table.rows[0].get_cell('continent'),
            self.continent.name
        )
