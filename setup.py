#!/usr/bin/env python

from setuptools import setup
import versioneer


setup(
    name='pionic',
    version=versioneer.get_version(),
    description='A Python 3 library for the Ion format.',
    author='Tony Locke',
    author_email='tlocke@tlocke.org.uk',
    url='https://github.com/tlocke/pionic',
    cmdclass=versioneer.get_cmdclass(),
    packages=[
        'pionic', 'pionic.antlr'],
    install_requires=[
        'antlr4-python3-runtime==4.7',
        'arrow==0.10.0'])
