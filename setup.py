#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(name='HE Encryption',
      version='1.0',
      description='The first He encryption implementation',
      url='http://github.com/MatufA/he-encription',
      author='',
      author_email='',
      license='MIT',
      packages=['he-encryption'],
      install_requires=open('requirements.txt', 'r').readlines(),
      zip_safe=False)
