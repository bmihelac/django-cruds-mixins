from django_webtest import WebTest

from django.utils.translation import ugettext as _

from cruds import utils as cruds_utils
from cruds_mixins.utils.text import (
    create_model_title,
    edit_model_title,
)

from .testapp.models import Author
from . import test_helper


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

        edit_label = _('edit')
        self.assertContains(response, edit_label)
        response = response.click(edit_label)
        delete_label = _('delete')
        self.assertContains(response, delete_label)
        response = response.click(delete_label)
        form = response.form
        response = form.submit()
        response = response.follow()
        self.assertContains(response, _('Record has been deleted.'))
        self.assertNotContains(response, 'BarFoo')

    def test_filters(self):
        self.author = test_helper.create_author(name='BarFoo')
        url = cruds_utils.crud_url(Author, cruds_utils.ACTION_LIST)
        response = self.app.get(url)
        form = response.forms[0]
        form['name'] = 'foo'
        response = form.submit()
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'BarFoo')

    def test_bulk_actions(self):
        self.author = test_helper.create_author()
        url = cruds_utils.crud_url(Author, cruds_utils.ACTION_LIST)
        response = self.app.get(url)

        form = response.forms[1]
        form['select_all'] = True
        response = form.submit(name='action', value='bulk_activate')
        self.assertEqual(response.status_code, 302)

        response = response.follow()
        self.assertContains(response, 'Bulk activate successful')

    def test_bulk_actions_with_intermediate_view(self):
        self.author = test_helper.create_author()
        url = cruds_utils.crud_url(Author, cruds_utils.ACTION_LIST)
        response = self.app.get(url)

        form = response.forms[1]
        form['select_all'] = True
        response = form.submit(
            name='action',
            value='bulk_activate_with_confirmation'
        )
        self.assertEqual(response.status_code, 200)

        form = response.form
        response = form.submit(name='submit')

        response = response.follow()
        self.assertContains(response, 'activated')
