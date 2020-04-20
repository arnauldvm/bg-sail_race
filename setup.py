#!/usr/bin/env python

from os.path import isdir
from setuptools import setup, find_packages
from shutil import rmtree

egg_info_dir = 'sail_race.egg-info'
if isdir(egg_info_dir):
    rmtree(egg_info_dir)

setup(
    entry_points={
        'console_scripts': ['sail_race = sail_race.cli:main']
    },
    packages=find_packages(),
)
