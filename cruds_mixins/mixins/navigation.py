# -*- coding: utf-8 -*-
from __future__ import unicode_literals


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
