from django.db import models

from cruds import utils as cruds_utils
from .managers import AuthorQuerySet


class Continent(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Continent'

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100)
    continent = models.ForeignKey(
        Continent,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return cruds_utils.crud_url(self, cruds_utils.ACTION_DETAIL)


class Author(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    country = models.ForeignKey(
        Country,
        verbose_name=Country._meta.verbose_name,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    active = models.BooleanField(
        'active',
        default=True,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return cruds_utils.crud_url(self, cruds_utils.ACTION_DETAIL)

    objects = AuthorQuerySet.as_manager()
