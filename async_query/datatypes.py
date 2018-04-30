# -*- coding: utf-8 -*-
"""Main module."""

import json
import logging
from collections import Counter, defaultdict

LOGGER = logging.getLogger('default')


class DataDict(defaultdict):
    """Base class to create nested dicts for data structure"""

    def __str__(self):
        return self.json

    @property
    def json(self):
        """
        Returns:
            str:  JSON formatted data
        """
        return json.dumps(self)

    @property
    def data(self):
        """
        Returns:
            dict: JSON formatted data
        """
        return json.loads(self.json)

    def update(self, *args):
        logging.debug('Skipping updating %s: %s', self.__class__, args)


class ApplicationData(DataDict):
    """
    {
        'application': {
            'version': Counter()
        }
    }
    """

    class VersionData(DataDict):
        """
        Stats counter per version
        { str(): Counter() }
        """

        def __init__(self, *args):  # pylint: disable=unused-argument
            super().__init__(Counter)

    def __init__(self, *args):  # pylint: disable=unused-argument
        self._keys = {
            'app_str': 'Application',
            'ver_str': 'Version',
            'total_str': 'Request_Count',
            'success_str': 'Success_Count',
            'error_str': 'Error_Count'
        }
        super().__init__(self.VersionData)

    @property
    def summary_data(self):
        """
        Returns:
            dict: JSON formatted data
        """
        return json.loads(self.summary)

    @property
    def summary(self):
        """
        Returns:
            str:  JSON formatted data
        """
        results = defaultdict(lambda: defaultdict(dict))
        for app, adata in sorted(self.data.items()):
            for ver, vdata in sorted(adata.items()):
                results[app][ver] = vdata[self._keys['success_str']] / vdata[self._keys[
                    'total_str']]

        return json.dumps(results)

    def _check_data(self, data):
        data = data or dict()
        ret = True
        if not set(self._keys.values()) <= data.keys():
            LOGGER.info('Missing data: %s', data)
            ret = False
        elif not data[self.
                      _keys['success_str']] + data[self.
                                                   _keys['error_str']] == data[self.
                                                                               _keys['total_str']]:
            LOGGER.info('Bad data: %s', data)
            ret = False
        return ret

    def update(self, data_in):  # pylint: disable=arguments-differ
        if self._check_data(data_in):
            data = data_in.copy()

            for item in [self._keys['app_str'], self._keys['ver_str']]:
                del data[item]
            self[data_in.get(self._keys['app_str'])][data_in.get(
                self._keys['ver_str'])].update(data)
        super().update(data_in)


if __name__ == "__main__":
    pass
