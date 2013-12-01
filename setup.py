#!/usr/bin/env python
import sys

from setuptools import setup, find_packages

if sys.version_info < (2, 7):
    raise Exception("This package requires Python 2.7 or higher.")

setup(
    name='geofences',
    version='0.1',
    description='Geofences for tracking objects in 2-D Euclidean space',
    author='Bryan Deeney',
    author_email='bdeeney@pobox.com',
    packages=find_packages(exclude=['tests.*', 'tests']),
    test_suite='nose.collector',
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'blinker',
        'colorama',
        'mock',
        'nose',
        'termcolor',
    ],
)
