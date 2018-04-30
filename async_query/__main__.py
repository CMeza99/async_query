# -*- coding: utf-8 -*-
"""Console script for requests_cli_example."""

import logging
import logging.config
import os

from fire import Fire
import yaml

from .cli import run


def main():
    """
    Generate CLI
    """
    with open(os.path.join(os.path.split(os.path.realpath(__file__))[0], 'logging.conf'),
              'r') as config_file:
        logging_conf = next(yaml.safe_load_all(config_file))
    logging.config.dictConfig(logging_conf)
    Fire(run)


if __name__ == "__main__":
    main()
