====================
async_query
====================


.. image:: https://img.shields.io/travis/cmeza99/async_query.svg
        :target: https://travis-ci.org/cmeza99/async_query


A small Python all to query servers' status endpoint for data.
This is a toy project meant for me to become familiar with Python 3.6 and asyncio.

Install:

.. code-block::

    python setup.py

Usage:

.. code-block::

    Args:
        servers_file: file to read line separated list
        output_file: writes json data

    Usage:       async_query [--servers_file SERVERS_FILE] [--output_file OUTPUT_FILE]

Sample Output:

.. code-block::

    CoreApp:
      1.0.0: 0.9
      1.0.0-beta: 0.9
    MyApp:
      10.0.1: 0.99
    SillyApp:
      2.0.0: 1.0
      2.0.1: 1.0
      2.1.0-rc2: 0.99


TODOs
--------

- non-blocking logging
- clean up tests
- docstrings
- set loglevel from cli param
- read server list from stdin
- adjustable timeouts
- retry failed connection
- tls, cert chaining, etc
- generate docs


Free software: MIT license
