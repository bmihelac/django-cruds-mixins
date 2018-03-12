from django_tables2 import Table
from cruds_mixins.tables.tables import StyledTable

from .models import (
    Author,
    Country,
)


class CountryTable(StyledTable):
    class Meta(StyledTable.Meta):
        model = Country
        non_orderable_fields = ('name',)


class AuthorTable(Table):
    class Meta:
        model = Author
