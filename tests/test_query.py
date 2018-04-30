# -*- coding: utf-8 -*-
# pylint: disable=empty-docstring,missing-docstring,protected-access
""" """

from pprint import pprint
from aioresponses import aioresponses

from async_query import query
from . import helpers


def test_bad_data():
    dataset, dataset_response = helpers.load('bad_data')
    servers = list()
    with aioresponses() as mocked:
        for data in dataset:
            for server, response in data.items():
                servers.append(server)
                url = query._server_urls([server])[0]
                mocked.get(url, status=200, body=str(response))
        results = query.main(servers, semaphores=10)
    pprint(results.data)
    assert results.data == dataset_response


def test_new_apps():
    dataset, dataset_response = helpers.load('new_apps')
    servers = list()
    with aioresponses() as mocked:
        for data in dataset:
            for server, response in data.items():
                servers.append(server)
                url = query._server_urls([server])[0]
                mocked.get(url, status=200, body=str(response))
        results = query.main(servers, semaphores=10)
    pprint(results.data)
    assert results.data == dataset_response


def test_new_version():
    tests = ['new_apps', 'new_versions']
    servers = list()
    with aioresponses() as mocked:
        for test in tests:
            print(test)
            dataset, dataset_response = helpers.load(test)
            # print(dataset)
            for data in dataset:
                for server, response in data.items():
                    servers.append(server)
                    url = query._server_urls([server])[0]
                    mocked.get(url, status=200, body=str(response))
            print(servers)
        results = query.main(servers, semaphores=10)
        pprint(results.data)
    assert results.data == dataset_response
