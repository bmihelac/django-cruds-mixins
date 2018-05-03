from datetime import date

from django.test.html import parse_html
import rules

from .testapp.models import Author


def create_author(**kwargs):
    defaults = {
        'name': 'Foo bar',
        'birthday': date(2000, 1, 1),
    }
    defaults.update(kwargs)
    return Author.objects.create(**defaults)


def reset_ruleset():
    ruleset = rules.permissions.permissions
    for k in list(ruleset.keys()):
        ruleset.pop(k)


def semantic_html(content):
    """Returns html for semantic comparison.
    """
    return str(parse_html(content.decode('utf-8')))
