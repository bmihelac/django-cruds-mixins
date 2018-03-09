from cruds.urls import crud_urls

from .models import Author

from cruds_mixins.views import crud


urlpatterns = crud_urls(
    Author,
    list_view=crud.CRUDListView.as_view(model=Author),
    detail_view=crud.CRUDDetailView.as_view(model=Author),
    url_prefix='author/',
)
