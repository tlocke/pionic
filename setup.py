#!/usr/bin/env python

from setuptools import setup
import versioneer


setup(
    name='pion',
    version=versioneer.get_version(),
    description='A Python 3 library for the Ion format.',
    author='Tony Locke',
    author_email='tlocke@tlocke.org.uk',
    url='https://github.com/tlocke/pion',
    cmdclass=versioneer.get_cmdclass(),
    packages=[
        'pion', 'pion.antlr'],
    install_requires=[
        'antlr4-python3-runtime==4.7',
        'arrow==0.10.0'])
