from django.test import TestCase
from django.views.generic import TemplateView

from cruds_mixins.mixins import navigation


class NavigationTest(TestCase):

    def test_navigation_item(self):
        navigation.NavigationItem(
            title='foo',
            url='/'
        )


class ActionsMixinTest(TestCase):

    def test_get_actions(self):

        class MyView(navigation.ActionsMixin, TemplateView):
            pass

        view = MyView()
        self.assertIn(
            'actions',
            view.get_context_data(),
            'should add actions to context'
        )
