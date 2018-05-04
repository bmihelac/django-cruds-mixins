from django.test import TestCase
from django.views.generic import ListView
from django.test import RequestFactory

from cruds_mixins.mixins.export import ExportMixin
from cruds_mixins.mixins.bulk_actions import BulkActionsMixin
from import_export.resources import ModelResource

from .testapp.models import Author
from . import test_helper


class MyView(ExportMixin, BulkActionsMixin, ListView):
    model = Author


class AuthorResource(ModelResource):
    class Meta:
        model = Author
        fields = ('name',)


class MyView2(MyView):
    export_resource_class = AuthorResource


class ExportMixinTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.author = test_helper.create_author()

    def test_bulk_export(self):
        response = MyView.as_view()(self.factory.post('', data={
            'action': 'bulk_export',
            'selection': [self.author.pk]
        }))
        self.assertEqual(
            response.content,
            b'id,name,birthday,country,active\r\n1,Foo bar,2000-01-01,,1\r\n'
        )
        self.assertEqual(
            response._headers['content-type'],
            ('Content-Type', 'text/csv')
        )

    def test_bulk_export_with_resource_class(self):
        response = MyView2.as_view()(self.factory.post('', data={
            'action': 'bulk_export',
            'selection': [self.author.pk]
        }))
        self.assertEqual(
            response.content,
            b'name\r\nFoo bar\r\n'
        )

    def test_can_export(self):
        class MyView3(MyView):
            def can_export(self):
                return False

        view = MyView3.as_view()
        response = view(self.factory.get(''))
        bulk_actions = response.context_data['bulk_action_actions']
        self.assertEqual(
            len(bulk_actions),
            0,
            'should not have bulk actions'
        )

        response = MyView2.as_view()(self.factory.post('', data={
            'action': 'bulk_export',
            'selection': [self.author.pk]
        }))
