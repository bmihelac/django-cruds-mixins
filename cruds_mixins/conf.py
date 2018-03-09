from django.conf import settings

from appconf import AppConf


class CrudsMixinsConf(AppConf):
    DEFAULT_SKIP_FIELDS = ['id']
