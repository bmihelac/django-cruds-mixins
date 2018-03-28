=============================
django-cruds-mixins
=============================

.. image:: https://badge.fury.io/py/django-cruds-mixins.svg
    :target: https://badge.fury.io/py/django-cruds-mixins

.. image:: https://travis-ci.org/bmihelac/django-cruds-mixins.svg?branch=master
    :target: https://travis-ci.org/bmihelac/django-cruds-mixins

.. image:: https://codecov.io/gh/bmihelac/django-cruds-mixins/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/bmihelac/django-cruds-mixins

EXPRERIMENTAL SOFTWARE! Do not use!

django-cruds-mixins integrates several libraries to enable easy, fast and
predicatable creation of admin panels and applications.

Features
--------

* list, create, update, detail, delete views for your models

* customizable tables with orderable columns, pagination and automatic links
  for ForeignKey fields, easily customizable with *django-tables2*

* search fiters based on model fields with *django-filter*

* permissions creation and integration with *django-rules*

* advanced forms with *django-crispy-forms*

* selections and bulk actions

* utils for creating URLconfs, permissions, filtersets, tables

Documentation
-------------

The full documentation is at https://django-cruds-mixins.readthedocs.io.

Quickstart
----------

Install django-cruds-mixins::

    pip install django-cruds-mixins

Add django-cruds-mixin and related apps to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'rules.apps.AutodiscoverRulesConfig',
        'crispy_forms',
        'django_tables2',
        'cruds',
        'cruds_mixins',
        ...
    )

Add the *django-rules* authentication backend for using permissions.

.. code-block:: python

    AUTHENTICATION_BACKENDS = (
        'rules.permissions.ObjectPermissionBackend',
        'django.contrib.auth.backends.ModelBackend',
    )

Add django-cruds-mixins's URL patterns:

.. code-block:: python

    from cruds_mixins import urls as cruds_mixins_urls


    urlpatterns = [
        ...
        url(r'^', include(cruds_mixins_urls)),
        ...
    ]

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
