# -*- coding: utf-8 -*-
# pylint: disable=empty-docstring,missing-docstring,protected-access
""" """

from pprint import pprint
import yaml

from async_query import datatypes
from .helpers import load_data


class TestApplicationData():
    appdata = datatypes.ApplicationData()

    def updating(self, dataset, assert_update=True):
        """Check each app as it gets included"""
        dataset = dataset or dict()
        for data in dataset:
            for response in data.values():
                self.appdata.update(response)
                if assert_update:
                    check_data = {
                        response[self.appdata._keys['app_str']]: {
                            response[self.appdata._keys['ver_str']]:
                            self.appdata.data[response.get(
                                self.appdata._keys['app_str'])][response.get(
                                    self.appdata._keys['ver_str'])]
                        }
                    }
                    test_data = {
                        response.pop(self.appdata._keys['app_str']): {
                            response.pop(self.appdata._keys['ver_str']): response
                        }
                    }
                    pprint(self.appdata.data)
                    assert check_data == test_data

    def loading(self, testname=None, asserts=True):
        dataset = load_data(testname + '.yaml')
        dataset_response = load_data(testname + '_response.json')
        self.updating(dataset, asserts)
        if asserts:
            pprint(self.appdata.data)
            assert dataset_response == self.appdata.data
        return dataset_response

    def test_return_type(self):
        assert isinstance(self.appdata, dict)
        assert isinstance(self.appdata.json, str)

    def test_bad_data(self):
        """Test not to include bad data"""
        assert self.loading('bad_data', asserts=False) == self.appdata.data

    def test_new_apps(self):
        """Test adding new applications"""
        self.loading('new_apps')
        assert self.appdata.summary_data == {"CoreApp": {"1.0.0-beta": 0.9}, "MyApp": {"10.0.1": 0.99}, "SillyApp": {"2.0.0": 1.0}}

    def test_new_version(self):
        """Test adding new versions to existing applications"""
        self.loading('new_versions')

    def test_update_counter_version(self):
        """Test incrementing data by replaying same data"""
        self.loading('new_apps', asserts=False)
        self.loading('new_versions', asserts=False)
        assert self.loading('update_counter', asserts=False) == self.appdata.data

    def test_summary(self):
        """Test percentages are returned"""
        print(yaml.dump(self.appdata.summary_data, default_flow_style=False))
        assert self.appdata.summary_data == {"CoreApp": {"1.0.0": 0.9, "1.0.0-beta": 0.9}, "MyApp": {"10.0.1": 0.99}, "SillyApp": {"2.0.0": 1.0, "2.0.1": 1.0, "2.1.0-rc2": 0.99}}
