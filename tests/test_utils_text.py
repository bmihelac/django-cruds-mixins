from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import force_text
from django.test import TestCase

from cruds_mixins.utils import text

from .testapp.models import Author


class TestUtilsText(TestCase):

    def test_create_model_title(self):
        res = text.create_model_title(Author)
        self.assertEqual(force_text(res), 'New Author')


    def test_edit_model_title(self):
        res = text.edit_model_title(Author)
        self.assertEqual(force_text(res), 'Edit Author')
