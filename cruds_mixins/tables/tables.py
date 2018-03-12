import django_tables2 as tables

from .columns import (
    ViewLinkColumn,
    SelectionColumn,
)


class StyledTable(tables.Table):
    """
    Bootstrap style.

    Abilities:

    `Meta.non_orderable_fields` disable sorting for specified fields
    """

    class Meta:
        attrs = {"class": "table table-bordered table-striped table-hover table--toggle-columns"}
        non_orderable_fields = []

    def __init__(self, *args, **kwargs):
        super(StyledTable, self).__init__(*args, **kwargs)
        for field in self.Meta.non_orderable_fields:
            self.base_columns[field].orderable = False


class DefaultTable(StyledTable):
    """
    Default django_tables2 table.

    Includes:

        * view_link

            If object detail view is different than default, add view_link::

                view_link = ViewLinkColumn(
                    viewname='viewname',
                    kwargs={
                        'slug': A('slug'),
                    },
                )

    """
    selection = SelectionColumn()
    view_link = ViewLinkColumn()

    class Meta(StyledTable.Meta):
        sequence = ('...', 'view_link')


def table_factory(model, fields):
    meta = type('Meta',
                (DefaultTable.Meta, object), {
                    'model': model,
                    'fields': fields,
                })
    table = type(str('%sTable' % model._meta.object_name),
                 (DefaultTable,), {'Meta': meta})
    return table
