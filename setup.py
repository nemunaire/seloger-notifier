#!/usr/bin/env python3

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = 1.0

with open('requirements.txt', 'r') as f:
    requires = [x.strip() for x in f if x.strip()]

#with open('test-requirements.txt', 'r') as f:
#    test_requires = [x.strip() for x in f if x.strip()]

setup(
    name = "seloger",
    version = version,
    description = "Basic SDK to interact with seloger.com API",
    long_description = open('README.md').read(),

    author = 'nemunaire',
    author_email = 'nemunaire@nemunai.re',

    url = 'https://github.com/nemunaire/seloger-notifier',
    license = 'AGPLv3',

    classifiers = [
        'Intended Audience :: Information Technology',

        'License :: OSI Approved :: GNU Affero General Public License v3',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords = 'house seloger',

    provides = ['seloger'],

    install_requires = requires,

    packages=[
        'seloger',
    ],

    scripts=[
        'bin/seloger-notifier',
    ],
)
