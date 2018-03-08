=====
Usage
=====

To use django-cruds-mixins in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'cruds_mixins.apps.CrudsMixinsConfig',
        ...
    )

Add django-cruds-mixins's URL patterns:

.. code-block:: python

    from cruds_mixins import urls as cruds_mixins_urls


    urlpatterns = [
        ...
        url(r'^', include(cruds_mixins_urls)),
        ...
    ]
