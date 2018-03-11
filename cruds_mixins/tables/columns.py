from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import force_text
from django.db import models
from django.urls import (
    NoReverseMatch,
    reverse,
)
from django_tables2.utils import AttributeDict

from django_tables2.columns.base import library
from django_tables2.columns.linkcolumn import (
    BaseLinkColumn,
    LinkColumn,
)
from django_tables2.columns import (
    CheckBoxColumn,
    Column,
    BooleanColumn,
)
from cruds.utils import (
    crud_url_name,
    ACTION_DETAIL,
    crud_url,
)


@library.register
class FKColumn(BaseLinkColumn):
    """
    django-tables2 column that renders link to ForeignKey if it exists.
    """

    def render(self, value, record, bound_column):
        # if table is in popup skip link
        if getattr(bound_column.table, 'is_popup', False):
            return value
        try:
            url = reverse(
                crud_url_name(type(value), ACTION_DETAIL),
                kwargs={'pk': value.pk})
        except NoReverseMatch:
            return value
        return self.render_link(url, record, value)

    @classmethod
    def from_field(cls, field):
        if isinstance(field, models.ForeignKey):
            return cls(verbose_name=field.verbose_name)


class ViewLinkColumn(LinkColumn):
    """
    Action column for table.

    Arguments:

        ``action`` - action type (detail, update)
    """

    def __init__(self,
                 viewname=None,
                 accessor=None,
                 verbose_name=None,
                 action_name=None,
                 action=None,
                 *args, **kwargs):
        if accessor is None:
            accessor = 'pk'
        if verbose_name is None:
            verbose_name = _('Actions')
        if action_name is None:
            action_name = _('View')
        self.action_name = action_name
        self.action = action
        super(ViewLinkColumn, self).__init__(viewname,
                                             accessor=accessor,
                                             verbose_name=verbose_name,
                                             orderable=False,
                                             *args,
                                             **kwargs)

    def render(self, value, record, bound_column):
        if self.viewname:
            try:
                return super(ViewLinkColumn, self).render(
                    self.action_name, record, bound_column)
            except NoReverseMatch:
                return ""
        if self.action:
            url = crud_url(record, self.action)
            return self.render_link(url, record, self.action_name)
        if hasattr(record, 'get_absolute_url'):
            url = record.get_absolute_url()
            return self.render_link(url, record, self.action_name)
        try:
            url = crud_url(record, 'detail')
            return self.render_link(url, record, self.action_name)
        except NoReverseMatch:
            return ""


class SelectionColumn(CheckBoxColumn):

    def __init__(self, *args, **kwargs):
        mykwargs = {
            'accessor': 'pk',
            'attrs': {
                "th__input": {"data-select-all": ""},
            },
            'orderable': False,
        }
        super(SelectionColumn, self).__init__(*args, **mykwargs)


class LinkDetail(BaseLinkColumn):
    """
    Render column as link to detail view.
    """

    def render(self, value, record, bound_column):
        try:
            url = record.get_absolute_url()
        except NoReverseMatch:
            return value
        except AttributeError:
            return value
        text = getattr(record, 'text', unicode(record))
        return self.render_link(url, record, value, {
            'data-pk': record.pk,
            'data-text': text,
        })


class StatusColumn(Column):
    """
    Display choice.
    """

    def __init__(self, field_name, choices, *args, **kwargs):
        self.field_name = field_name
        self.choices = choices
        super(StatusColumn, self).__init__(*args, **kwargs)

    def render(self, value, record, *args, **kwargs):
        value = getattr(record, self.field_name)
        label = self.choices[value]
        return label


class ManyToManyColumn(Column):
    #Using of m2m and related set in accessor quietly fails with Django 1.7 and later
    #https://github.com/bradleyayers/django-tables2/issues/229

    def __init__(self, m2m_field, *args, **kwargs):
        kwargs['orderable'] = False
        kwargs['accessor'] = 'id'
        self.m2m_field = m2m_field
        super(ManyToManyColumn, self).__init__(*args, **kwargs)

    def render(self, value, record, *args, **kwargs):
        return ", ".join([force_text(item)
                          for item in getattr(record, self.m2m_field).all()])


@library.register
class MyBooleanColumn(BooleanColumn):
    """Boolean column with fa icons.
    """
    def __init__(self, null=False, yesno=None, **kwargs):
        if yesno is None:
            yesno = (
                mark_safe('<i class="fa fa-check" aria-hidden="true"></i>'),
                mark_safe('<i class="fa fa-times" aria-hidden="true"></i>'),
            )
        super(MyBooleanColumn, self).__init__(null, yesno, **kwargs)

    def render(self, value):
        value = bool(value)
        text = self.yesno[int(not value)]
        html = '<span %s>%s</span>'
        attrs = {"class": 'boolean-icon--' + str(value).lower()}
        attrs.update(self.attrs.get("span", {}))
        return mark_safe(html % (AttributeDict(attrs).as_html(), text))
