from django.conf import settings

from appconf import AppConf


class CrudsMixinsConf(AppConf):
    DEFAULT_SKIP_FIELDS = ['id']
    DEFAULT_PERMISSION_CLASS = 'cruds_mixins.permission_classes.AllowAny'
