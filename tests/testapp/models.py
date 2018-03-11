from django.db import models

from cruds import utils as cruds_utils


class Author(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateTimeField()
    active = models.BooleanField(
        'active',
        default=False,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return cruds_utils.crud_url(self, cruds_utils.ACTION_DETAIL)
