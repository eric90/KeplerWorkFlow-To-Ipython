#!/usr/bin/env python3
# encoding: UTF-8


from distutils.core import setup

desc = """\
KeplerWorkFlow to Ipython Notebook
Kepler website:
https://kepler-project.org/

"""
setup(name='KeplerMagic',
      version='1.0',
      long_description=desc,
      py_modules=['KeplerFunc','KeplerLib'],
      )