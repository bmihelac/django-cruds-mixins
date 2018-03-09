from django_webtest import WebTest

from django.utils.translation import ugettext as _

from cruds import utils as cruds_utils
from cruds_mixins.utils.text import (
    create_model_title,
    edit_model_title,
)

from .testapp.models import Author


class IntegrationTest(WebTest):

    def setUp(self):
        super(IntegrationTest, self).setUp()

    def test_default(self):
        url = cruds_utils.crud_url(Author, cruds_utils.ACTION_LIST)
        response = self.app.get(url)
        self.assertEqual(response.status_code, 200)

        create_label = create_model_title(Author)
        self.assertContains(response, create_label)

        response = response.click(create_label)
        form = response.form
        self.assertIn('name', form.fields)
        self.assertIn('birthday', form.fields)
        form['name'] = 'foo bar'
        form['birthday'] = '2001-01-01'
        response = form.submit()

        self.assertEqual(response.status_code, 302)
        response = response.follow()

        self.assertContains(response, 'foo bar')

        edit_label = _('edit')
        self.assertContains(response, edit_label)
        response = response.click(edit_label)

        form = response.form
        self.assertIn('name', form.fields)
        self.assertIn('birthday', form.fields)
        form['name'] = 'BarFoo'
        response = form.submit()
        self.assertEqual(response.status_code, 302)
        response = response.follow()
        self.assertContains(response, 'BarFoo')
