import django_tables2 as tables

from .columns import (
    ViewLinkColumn,
    SelectionColumn,
)


class StyledTable(tables.Table):
    """
    Bootstrap style.

    Abilities:

        * Meta.non_orderable_fields override to disable sorting for specified
        fields
    """

    class Meta:
        attrs = {"class": "table table-bordered table-striped table-hover table--toggle-columns"}
        non_orderable_fields = []
        hidden_initial = []

    def __init__(self, *args, **kwargs):
        super(StyledTable, self).__init__(*args, **kwargs)
        for field in self.Meta.non_orderable_fields:
            self.base_columns[field].orderable = False

    def table_name(self):
        return self.__class__.__name__

    def get_default_hidden_columns(self):
        return self.Meta.hidden_initial

    def get_default_table_config(self):
        hidden = self.get_default_hidden_columns()
        return dict([
            (column.name, {'show': 0 if column.name in hidden else 1})
            for column in self.columns.all()
        ])


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
