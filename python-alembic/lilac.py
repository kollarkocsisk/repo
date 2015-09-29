#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'
depends = ['python-editor']

def pre_build():
  # aur_pre_build()
  pypi_pre_build(depends=['python-editor'])

def post_build():
  pypi_post_build()

if __name__ == '__main__':
  single_main()

# vim:set ts=2 sw=2 et:
