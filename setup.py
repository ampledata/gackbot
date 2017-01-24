#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup for the GACKbot.

Source:: https://github.com/ampledata/gackbot
"""

import os
import sys
import setuptools

__title__ = 'gackbot'
__version__ = '0.0.1b1'
__author__ = 'Greg Albrecht <oss@undef.net>'
__copyright__ = 'Copyright 2017 Greg Albrecht'
__license__ = 'Apache License, Version 2.0'


def publish():
    """Function for publishing package to pypi."""
    if sys.argv[-1] == 'publish':
        os.system('python setup.py sdist')
        os.system('twine upload dist/*')
        sys.exit()


publish()


setuptools.setup(
    name=__title__,
    version=__version__,
    description='GACKbot',
    author='Greg Albrecht',
    author_email='oss@undef.net',
    packages=['gackbot'],
    package_data={'': ['LICENSE']},
    package_dir={'gackbot': 'gackbot'},
    license=open('LICENSE').read(),
    long_description=open('README.rst').read(),
    url='https://github.com/ampledata/gackbot',
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'requests >= 2.8.1',
        'slackbot'
    ],
    entry_points={'console_scripts': ['gackbot = gackbot.cmd:cli']}
)
