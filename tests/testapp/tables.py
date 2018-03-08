from django_tables2 import Table

from .models import Author


class AuthorTable(Table):
    class Meta:
        model = Author
