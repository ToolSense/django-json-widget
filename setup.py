#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Forked from https://github.com/jmrivas86/django-json-widget

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open("README.rst").read()
history = open("HISTORY.rst").read().replace(".. :changelog:", "")

setup(
    name="django-json-widget",
    version="2.0.1",
    description="""Django json widget is an alternative widget that makes it easy to edit the jsonfield field of django.""",
    long_description=readme + "\n\n" + history,
    author="José Manuel Rivas",
    author_email="jmrivas86@gmail.com",
    url="https://github.com/jmrivas86/django-json-widget",
    packages=[
        "django_json_widget",
    ],
    include_package_data=True,
    license="MIT",
    zip_safe=False,
    keywords="django-json-widget",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.2",
        "Framework :: Django :: 5.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
