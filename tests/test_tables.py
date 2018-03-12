from django.test import TestCase

import django_tables2 as tables
from cruds_mixins.tables.tables import (
    StyledTable,
)


class StyledTableTest(TestCase):

    def test_non_orderable_fields(self):

        class MyTable(StyledTable):
            column1 = tables.Column()
            column2 = tables.Column()

            class Meta(StyledTable.Meta):
                non_orderable_fields = ('column1',)

        table = MyTable([{}])
        self.assertFalse(table.base_columns['column1'].orderable)
