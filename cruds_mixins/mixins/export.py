from datetime import datetime

from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse

from import_export import resources
from import_export.formats.base_formats import CSV


class ExportMixin(object):
    """Mixin that adds export bulk action to CRUDListView.

    `export_resource_class` - resource class to use for export, default None
    """
    export_resource_class = None

    def can_export(self):
        return True

    def get_bulk_action_methods(self):
        bulk_actions = super(ExportMixin, self).get_bulk_action_methods()
        if self.can_export():
            bulk_actions.append('bulk_export')
        return bulk_actions

    def get_export_resource_class(self, queryset):
        if self.export_resource_class is None:
            return resources.modelresource_factory(queryset.model)
        return self.export_resource_class

    def get_export_basename(self):
        return self.model.__name__

    def get_export_filename(self):
        date_str = datetime.now().strftime('%Y-%m-%d')
        return "%s-%s.csv" % (
            self.get_export_basename(),
            date_str,
        )

    def prepare_export_queryset(self, queryset):
        return queryset

    def get_export_format(self):
        return CSV

    def bulk_export(self, request, action_name, selection, select_all,
                    queryset, *args, **kwargs):
        prepared_queryset = self.prepare_export_queryset(queryset)
        file_format = self.get_export_format()()
        resource_class = self.get_export_resource_class(prepared_queryset)
        data = resource_class().export(prepared_queryset)
        filename = self.get_export_filename()
        export_data = file_format.export_data(data)
        content_type = file_format.CONTENT_TYPE
        response = HttpResponse(export_data, content_type=content_type)
        response['Content-Disposition'] = 'attachment; filename=%s' % filename
        return response
    bulk_export.short_description = _('Export')
