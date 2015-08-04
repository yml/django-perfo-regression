#!/usr/bin/env python
from sys import exit

from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand

setup(
    name='template_perfo_regression',
    version='1.0',
    packages=find_packages(),
    package_data={
        'template_perfo_regression': ['templates/*.*']
    },
    include_package_data=True,
    install_requires=[]
)
