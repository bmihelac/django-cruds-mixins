from cruds import utils as cruds_utils
from cruds_mixins.views import crud
from cruds_mixins.mixins.messages import MessagesMixin
from cruds_mixins.mixins.bulk_actions import BulkSelectionActionBaseView

from .models import Author


class AuthorListView(crud.CRUDListView):
    model = Author
    bulk_actions = [
        'bulk_activate',
        'bulk_activate_with_confirmation',
    ]

    def bulk_activate(self, request, action_name, selection, select_all, queryset):
        queryset.update(active=True)
        return self.add_message_and_redirect(
            'Bulk activate successful',
            cruds_utils.crud_url(Author, cruds_utils.ACTION_LIST)
        )
    bulk_activate.short_description = 'Bulk activate'

    def bulk_activate_with_confirmation(self, request, action_name, selection, select_all, queryset):
        view = AuthorActivateView.as_view()
        return view(request, action_name, selection, select_all, queryset)
    bulk_activate_with_confirmation.short_description = 'Bulk activate with confirmation'


class AuthorActivateView(MessagesMixin, BulkSelectionActionBaseView):

    def get_title(self):
        return 'Bulk activate with confirmation'

    def form_valid(self, form):
        self.add_message('activated')
        return super().form_valid(form)
