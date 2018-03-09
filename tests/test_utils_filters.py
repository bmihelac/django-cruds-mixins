from django.test import TestCase

from cruds_mixins.utils import filters

from .testapp.models import Author


class FiltersTest(TestCase):

    def test_filterset_factory(self):
        filterset_class = filters.filterset_factory(Author, [
            'name',
        ])
        self.assertTrue(
            issubclass(filterset_class, filters.DefaultFilterSet)
        )
        self.assertTrue(
            issubclass(filterset_class.Meta, filters.DefaultFilterSet.Meta)
        )

        filterset = filterset_class()
        name = filterset.base_filters['name']
        self.assertEqual(
            name.lookup_expr,
            'icontains'
        )

        form = filterset.form
        self.assertIn('name', form.fields)
