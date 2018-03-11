from cruds.urls import crud_urls

from .models import Author

from cruds_mixins.views import crud
from . import views


fields = [
    'name',
    'birthday',
]

urlpatterns = crud_urls(
    Author,
    list_view=views.AuthorListView.as_view(),
    create_view=crud.CRUDCreateView.as_view(model=Author, fields=fields),
    update_view=crud.CRUDUpdateView.as_view(model=Author, fields=fields),
    delete_view=crud.CRUDDeleteView.as_view(model=Author),
    detail_view=crud.CRUDDetailView.as_view(model=Author),
    url_prefix='author/',
)
