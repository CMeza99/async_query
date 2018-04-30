# -*- coding: utf-8 -*-
# pylint: disable=empty-docstring,missing-docstring
""" """

import json
import os
import yaml


def load_data(data_file):
    datadir = os.path.join(os.path.dirname(__file__), 'data')
    status_responses = None

    with open(os.path.join(datadir, data_file)) as file:
        _, ext = os.path.splitext(file.name)
        if ext == ('.yaml' or '.yml'):
            status_responses = yaml.safe_load(file)
        elif ext == '.json':
            status_responses = json.load(file)

    return status_responses


def load(testname=None):
    dataset = load_data(testname + '.yaml')
    dataset_response = load_data(testname + '_response.json')
    return (dataset, dataset_response)


if __name__ == "__main__":
    pass
