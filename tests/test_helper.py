from datetime import date

from .testapp.models import Author


def create_author(**kwargs):
    defaults = {
        'name': 'Foo bar',
        'birthday': date(2000, 1, 1),
    }
    defaults.update(kwargs)
    return Author.objects.create(**defaults)
