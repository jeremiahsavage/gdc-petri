#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name = 'gdc-petri',
      author = 'Jeremiah H. Savage',
      author_email = 'jeremiahsavage@gmail.com',
      version = 0.3,
      description = 'petri net automation for gdc',
      url = 'https://github.com/jeremiahsavage/gdc-petri',
      license = 'Apache 2.0',
      packages = find_packages(),
      install_requires = [
          'SNAKES'
      ],
      classifiers = [
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
      ],
      entry_points={
          'console_scripts': ['gdc-petri=gdc-petri.__main__:main']
          },
)
