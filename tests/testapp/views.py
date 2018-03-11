from cruds import utils as cruds_utils
from cruds_mixins.views import crud

from .models import Author


class AuthorListView(crud.CRUDListView):
    model = Author
    bulk_actions = [
        'bulk_activate',
    ]

    def bulk_activate(self, request, action_name, selection, select_all, queryset):
        queryset.update(active=True)
        return self.add_message_and_redirect(
            'Bulk activate successful',
            cruds_utils.crud_url(Author, cruds_utils.ACTION_LIST)
        )
    bulk_activate.short_description = 'Bulk activate'
