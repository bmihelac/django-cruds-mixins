<a name="1.0.0"></a>
# 1.0.0 (2018-05-08)


### Bug Fixes

* RulesPermissions should pass instance ([da82a1a](https://github.com/bmihelac/django-cruds-mixins/commit/da82a1a))
* snapshot testing between platforms ([4a69d7a](https://github.com/bmihelac/django-cruds-mixins/commit/4a69d7a))


### feature

* raise 403 instead of login ([ba5175f](https://github.com/bmihelac/django-cruds-mixins/commit/ba5175f))


### Features

* add ExportMixin ([9a63fa4](https://github.com/bmihelac/django-cruds-mixins/commit/9a63fa4))
* add request when initializing FilterSet ([1b0c9fe](https://github.com/bmihelac/django-cruds-mixins/commit/1b0c9fe))
* move buttons CSS classes to config ([05f59f2](https://github.com/bmihelac/django-cruds-mixins/commit/05f59f2))
* snapshot TablesTest ([7bd7d0b](https://github.com/bmihelac/django-cruds-mixins/commit/7bd7d0b))


### BREAKING CHANGES

* All views now returns HTTP 403 Forbidden response
instead of redirecting to login page

see https://code.djangoproject.com/ticket/28379?cversion=0&cnum_hist=5