from django.utils.encoding import force_str
from django.db import models
from django.urls import (
    NoReverseMatch,
)
from django.utils.html import format_html

from django_tables2.columns.base import library
from django_tables2.columns.linkcolumn import (
    BaseLinkColumn,
    LinkColumn,
)
from django_tables2.columns import (
    CheckBoxColumn,
)
from django_tables2.utils import AttributeDict
from cruds.utils import (
    crud_url,
)
from django.utils.translation import gettext_lazy as _


@library.register
class FKColumn(BaseLinkColumn):
    """Column that renders link to ForeignKey if it exists."""

    def render(self, value, record, bound_column):
        try:
            url = value.get_absolute_url()
        except (AttributeError, NoReverseMatch):
            return force_str(value)
        attrs = AttributeDict((("href", url),))
        return format_html(
            "<a {attrs}>{text}</a>",
            attrs=attrs.as_html(),
            text=value,
        )

    @classmethod
    def from_field(cls, field, **kwargs):
        if isinstance(field, models.ForeignKey):
            return cls(verbose_name=field.verbose_name)


class ViewLinkColumn(BaseLinkColumn):
    """
    Action column for table.

    Arguments:

        ``action`` - action type (detail, update)
    """

    def __init__(
        self,
        accessor=None,
        verbose_name=None,
        action_name=None,
        action=None,
        *args,
        **kwargs
    ):
        if accessor is None:
            accessor = "pk"
        if verbose_name is None:
            verbose_name = _("Actions")
        if action_name is None:
            action_name = _("View")
        self.action_name = action_name
        self.action = action
        super().__init__(
            accessor=accessor,
            verbose_name=verbose_name,
            orderable=False,
            *args,
            **kwargs
        )

    def render(self, value, record, bound_column):
        if self.action:
            url = crud_url(record, self.action)
        else:
            url = record.get_absolute_url()
        attrs = AttributeDict((("href", url),))
        return format_html(
            "<a {attrs}>{text}</a>",
            attrs=attrs.as_html(),
            text=self.action_name,
        )


class SelectionColumn(CheckBoxColumn):
    def __init__(self, *args, **kwargs):
        mykwargs = {
            "accessor": "pk",
            "attrs": {
                "th__input": {"data-select-all": ""},
            },
            "orderable": False,
        }
        super(SelectionColumn, self).__init__(*args, **mykwargs)
