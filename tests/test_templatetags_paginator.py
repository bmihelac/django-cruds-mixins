from snapshottest.django import TestCase
from django.template import loader, Context
from django.core.paginator import Paginator, Page


class TestPaginatorTags(TestCase):

    def setUp(self):
        self.objects = [
            'object %d' % i
            for i in range(100)
        ]
        self.paginator = Paginator(self.objects, 5)
        self.template = loader.get_template('cruds_mixins/partials/pagination.html')

    def test_default(self):
        page = Page(self.objects, 1, self.paginator)
        c = {'page_obj': page, 'is_paginated': True}
        result = self.template.render(c)
        self.assertMatchSnapshot(result)

        page = Page(self.objects, 15, self.paginator)
        c = {'page_obj': page, 'is_paginated': True}
        result = self.template.render(c)
        self.assertMatchSnapshot(result)
