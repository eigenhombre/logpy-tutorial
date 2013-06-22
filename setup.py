#!/usr/bin/env python

from os.path import exists
from setuptools import setup, find_packages

setup(
    name='logpy-tutorial',
    # Your name & email here
    author='John Jacobsen',
    author_email='john@mail.npxdesigns.com',
    # If you had pyclojure.tests, you would also include that in this list
    packages=find_packages(),
    # Any executable scripts, typically in 'bin'. E.g 'bin/do-something.py'
    scripts=[],
    license='',
    description='Tutorial to teach myself and others LogPy',
    long_description=open('README').read() if exists("README") else "",
    install_requires=[
       "conttest",
       "nose",
       "logic",
    ],
    entry_points={'console_scripts': [
                   #'name = x.y.z:main',
                   ]},
)
