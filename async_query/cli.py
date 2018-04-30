# -*- coding: utf-8 -*-
"""CLI"""

import yaml

from . import query


def _get_servers(file=None):
    """
    Read in set of servers

    Returns:
        set: of servers

    TODO: read stdin
    """
    servers = set()
    if file:
        with open(file, 'r') as open_file:
            servers = set(line.strip() for line in open_file.read().splitlines())
    return servers


def run(*args, servers_file=None, output_file='data.json'):
    """Aggregates data from servers' statuses pages

    Args:
        servers_file: file to read line separated list
        output_file: writes json data
    """

    servers = _get_servers(servers_file)
    data = query.main(servers)
    print(yaml.dump(data.summary_data, default_flow_style=False))
    with open(output_file, 'w') as savefile:
        savefile.write(data.summary)


if __name__ == "__main__":
    pass
