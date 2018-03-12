from django.test import TestCase
from django.views.generic import ListView
from django.test import RequestFactory

from django_filters import FilterSet

from cruds_mixins.mixins.filter_mixin import (
    FilterMixin,
)

from .testapp.models import Author


class FilterMixinTest(TestCase):

    def test_filterset_fields(self):
        class MyView(FilterMixin, ListView):
            model = Author
            filterset_fields = ('name',)

        view = MyView()
        fields = view.get_filterset_fields()
        self.assertEqual(fields, ('name',))

    def test_filterset_exclude_fields(self):
        class MyView(FilterMixin, ListView):
            model = Author
            filterset_exclude_fields = ('name',)

        view = MyView()
        fields = view.get_filterset_fields()
        self.assertEqual(fields, ['birthday', 'country', 'active'])

    def test_filterset_false(self):
        class MyView(FilterMixin, ListView):
            model = Author
            filterset = False

        view = MyView()
        qs = Author.objects.all()
        self.assertIsNone(view.get_filter(qs))
        self.assertEqual(
            view.get_filtered_queryset(qs),
            qs,
            'should return unmodified queryset'
        )

    def test_with_filterset(self):
        FS = FilterSet

        class MyView(FilterMixin, ListView):
            model = Author
            filterset = FS

        view = MyView()
        self.assertEqual(
            view.get_filterset(),
            FS
        )
