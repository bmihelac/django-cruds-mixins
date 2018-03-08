# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import hashlib
import re

from datetime import date, timedelta

from django.utils.translation import ugettext_lazy as _
from django.utils import formats


def fill_field(field, text):
    """
    Helper to set predefined field value on link click.
    """
    template = '<a href="#" data-fill-field="{field}">{text}</a>'
    return template.format(
        field=field,
        text=text,
    )


def datelink(field, day=None, days=0):
    """
    <a href="#" data-insert-day="id_field">10.12.2014</a>
    """
    template = '<a href="#" data-insert-day="{field}">{day}</a>'
    if day is None:
        day = date.today()
    day = day + timedelta(days)
    return template.format(
        field=field,
        day=formats.date_format(day, 'SHORT_DATE_FORMAT')
    )


def create_model_title(model):
    return _('New %(model_name)s') % {
        'model_name': model._meta.verbose_name.capitalize()
    }


def edit_model_title(model):
    return _('Edit %(model_name)s') % {
        'model_name': model._meta.verbose_name.capitalize()
    }


def i18n_manage(name):
    return _('Manage %(name)s') % {'name': name},


def moneyfmt(val, currency_symbol=None):
    a = (u"%.02f" % val).replace(u'.', u',')
    reg = re.compile(r"(\d)(\d\d\d[.,])")
    while 1:
        a, count = re.subn(reg, r"\1.\2", a)
        if not count:
            break
    return u"%s %s" % (a, currency_symbol) if currency_symbol else a


def get_signature(text):
    """
    Returns md5 hash for given text.
    """
    return hashlib.md5(text).hexdigest()


def yes_or_no_text(val):
    return _('Yes') if val else _('No')


def to_excel_string(val):
    """
    Format value so to force Excel to interpret value as a string
    """
    return '="%s"' % val
