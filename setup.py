#!/usr/bin/env python

"""
This setup is suitable for "python setup.py develop" if setuptools.
"""
from setuptools import setup

from unit_conversion import __version__

setup(
    name = "unit_conversion",
    description='Physical Unit conversion utilties -- units useful for oil and chemical spill response',
    author='Christopher H. Barker',
    author_email='Chris.Barker@noaa.gov',
    url='https://github.com/NOAA-ORR-ERD/PyNUCOS',
    version = __version__,
    packages = ['unit_conversion'],
    )