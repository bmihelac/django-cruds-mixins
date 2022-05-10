#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_version(*file_paths):
    """Retrieves the version from cruds_mixins/__init__.py"""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


version = get_version("cruds_mixins", "__init__.py")


readme = open('README.rst').read()

setup(
    name='django-cruds-mixins',
    version=version,
    description="""Fast and predicatable creation of admin panels and applications""",
    long_description=readme,
    author='Bojan Mihelac',
    author_email='bmihelac@mihelac.org',
    url='https://github.com/bmihelac/django-cruds-mixins',
    packages=[
        'cruds_mixins',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=3.2,<4',
        'rules==3.3',
        'django-tables2==2.4.1',
        'django-appconf==1.0.5',
        'django-filter==2.4.0',
        'django-crispy-forms==1.14.0',
        'django-cruds>=2.0,<3',
        'django-import-export<3,>=2.8.0',
    ],
    zip_safe=False,
    keywords='django-cruds-mixins',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
