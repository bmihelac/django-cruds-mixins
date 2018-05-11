<a name="1.4.0"></a>
# [1.4.0](https://github.com/bmihelac/django-cruds-mixins/compare/v1.3.0...v1.4.0) (2018-05-11)


### Features

* use BEM css classes in templates ([1e415d4](https://github.com/bmihelac/django-cruds-mixins/commit/1e415d4))

<a name="1.3.0"></a>
# [1.3.0](https://github.com/bmihelac/django-cruds-mixins/compare/v1.2.1...v1.3.0) (2018-05-11)


### Features

* configurable default table css class ([41220f6](https://github.com/bmihelac/django-cruds-mixins/commit/41220f6))

<a name="1.2.1"></a>
## [1.2.1](https://github.com/bmihelac/django-cruds-mixins/compare/v1.2.0...v1.2.1) (2018-05-10)


### Bug Fixes

* include translations in distribution ([8626c4e](https://github.com/bmihelac/django-cruds-mixins/commit/8626c4e))

<a name="1.2.0"></a>
# [1.2.0](https://github.com/bmihelac/django-cruds-mixins/compare/v1.1.0...v1.2.0) (2018-05-10)


### Features

* release 1.2.0 ([b43761a](https://github.com/bmihelac/django-cruds-mixins/commit/b43761a))

<a name="1.1.0"></a>
# [1.1.0](https://github.com/bmihelac/django-cruds-mixins/compare/v1.0.0...v1.1.0) (2018-05-09)


### Features

* add translation catalog ([1536ae5](https://github.com/bmihelac/django-cruds-mixins/commit/1536ae5))

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
