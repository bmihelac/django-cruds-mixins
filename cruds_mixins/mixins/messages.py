from django.contrib import messages
from django.shortcuts import (
    redirect,
)


class MessagesMixin(object):

    def add_message(self, msg, msg_type=None, extra_tags=''):
        if not msg_type:
            msg_type = messages.INFO
        messages.add_message(self.request, msg_type, msg, extra_tags)

    def add_message_and_redirect(self, msg, url, msg_type=None, extra_tags=''):
        self.add_message(msg, msg_type, extra_tags)
        return redirect(url)

    def add_error_message_and_redirect(self, msg, url):
        return self.add_message_and_redirect(msg, url, messages.ERROR, 'danger')
