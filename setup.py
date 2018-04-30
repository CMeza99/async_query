#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=invalid-name

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['fire>=0.1.3', 'aiodns>=1.1.1', 'aiohttp>=3.1.3']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', 'flake8', 'pylint', ]

setup(
    author="Carlos Meza",
    author_email='hire@carlosmeza.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    description="Learning Python3 and asyncio",
    entry_points={
        'console_scripts': [
            'async_query=async_query.__main__:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='async_query',
    name='async_query',
    packages=find_packages(include=['async_query']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/cmeza99/async_query',
    version='0.1.0',
    zip_safe=False,
)
