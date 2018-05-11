from django.test import RequestFactory
from snapshottest.django import TestCase

from django_tables2 import Table
from cruds_mixins.mixins.tables import (
    TableView
)

from .testapp.models import Author
from .testapp.tables import AuthorTable
from . import test_helper


def test_default(db, rf, snapshot):
    view = TableView.as_view(
        model=Author,
        template_name='testapp/table.html'
    )
    response = view(rf.get(''))
    assert response.status_code, 200
    response.render()
    snapshot.assert_match(test_helper.semantic_html(response.content))


def test_custom_table(db, rf, snapshot):
    view = TableView.as_view(
        model=Author,
        template_name='testapp/table.html',
        table=AuthorTable
    )
    response = view(rf.get(''))
    assert response.status_code, 200
    response.render()
    snapshot.assert_match(test_helper.semantic_html(response.content))


def test_with_table_fields(db, rf, snapshot):
    view = TableView.as_view(
        model=Author,
        template_name='testapp/table.html',
        table_fields=('name',)
    )
    response = view(rf.get(''))
    assert response.status_code, 200
    response.render()
    content = response.content.decode()
    assert 'name' in content
    assert 'birthday' not in content
