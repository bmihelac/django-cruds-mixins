from django.contrib.auth.models import AnonymousUser

from cruds_mixins.views.crud import (
    CRUDListView,
    CRUDUpdateView,
)

from .testapp.models import Author
from . import test_helper


def test_list(db, rf, snapshot):
    view = CRUDListView.as_view(model=Author)
    request = rf.get('')
    request.user = AnonymousUser
    response = view(request)
    response.render()
    snapshot.assert_match(test_helper.semantic_html(response.content))


class MyView(CRUDUpdateView):
    model = Author
    fields = ('name', )

    def get_message(self):
        return None


def test_update(db, rf, snapshot, monkeypatch):
    request = rf.post('', {'name': 'aaa'})
    request.user = AnonymousUser
    author = test_helper.create_author()
    MyView.as_view()(request, pk=author.pk)

    add_message_called = False

    def add_message(*args, **kwargs):
        nonlocal add_message_called
        add_message_called = True

    monkeypatch.setattr('cruds_mixins.mixins.cruds.messages.add_message', add_message)
    assert add_message_called is False
