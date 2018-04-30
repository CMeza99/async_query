# -*- coding: utf-8 -*-
"""Main module."""

import logging
from ast import literal_eval
from asyncio import new_event_loop, Semaphore
from aiohttp import ClientSession, ClientError

from .datatypes import ApplicationData

LOGGER = logging.getLogger('default')


async def _fetch(session=None, url=None, timeout=10):
    try:
        async with session.get(url, timeout=timeout) as response:
            return await response.text()
    except ClientError as err:
        LOGGER.error('%s: %s', err.__class__.__name__, err)


def _server_urls(servers=None, page='status', protocol='http'):
    urls = ["{}://{}/{}".format(protocol, server, page) for server in servers]
    return urls


async def application_data(servers=None, semaphores=None, loop=None):
    """

    Args:
        servers:
        semaphores:
        loop:

    Returns:
        defaultdict: a dict of aggregated data

    """
    results = ApplicationData()
    async with Semaphore(semaphores, loop=loop):
        async with ClientSession(loop=loop) as session:
            urls = _server_urls(servers)
            for url in urls:
                response = await _fetch(session, url)
                if response:
                    try:
                        response_dict = literal_eval(response)
                    except Exception as err:  # pylint: disable=broad-except
                        LOGGER.error('%s: %s', err.__class__.__name__, err)
                    else:
                        results.update(response_dict)
    return results


def main(servers=None, semaphores=1024):
    """

    Args:
        servers:
        semaphores:

    Returns:
        defaultdict: a dict of aggregated data

    """
    loop = new_event_loop()
    try:
        data = loop.run_until_complete(application_data(servers, semaphores=semaphores))
    finally:
        loop.close()
    return data


if __name__ == "__main__":
    pass
