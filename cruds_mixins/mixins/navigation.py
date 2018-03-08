# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Separator(object):

    def __init__(self):
        pass

    def html(self):
        return '<div class="clearfix"></div>'


class NavigationItem(object):
    """
    Represent navigation item to use in pills, buttons.
    """

    def __init__(self, title, url, code=None, css_class=None, post=None,
                 action=None, value=None,
                 ):
        self.title = title
        self.url = url
        self.code = code
        self.css_class = css_class
        self.post = post
        self.action = action
        self.value = value


class NavigationMixin(object):
    """
    Mixin that provides navigation.
    """
    NAVIGATION_CODE = None

    def __init__(self, *args, **kwargs):
        super(NavigationMixin, self).__init__(*args, **kwargs)

    def get_navigation(self):
        """
        Return NavigationItem list.
        """
        return []

    def get_active_navigation(self):
        return self.NAVIGATION_CODE

    def get_context_data(self, *args, **kwargs):
        context = super(NavigationMixin, self).get_context_data(
            *args, **kwargs)
        context['navigation'] = self.get_navigation()
        context['navigation_active'] = self.get_active_navigation()
        return context


class ActionsMixin(object):
    """
    Mixin that provides ``actions`` context variable.
    """

    def get_actions(self):
        actions = []
        return actions

    def get_context_data(self, **kwargs):
        context = super(ActionsMixin, self).get_context_data(**kwargs)
        context['actions'] = self.get_actions()
        return context
