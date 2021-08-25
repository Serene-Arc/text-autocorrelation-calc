#!/usr/bin/env python3
# coding=utf-8

import argparse
import csv
import logging
import sys
from pathlib import Path

parser = argparse.ArgumentParser()
logger = logging.getLogger()


def _setup_logging(verbosity: int):
    logger.setLevel(1)
    stream = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('[%(asctime)s - %(name)s - %(levelname)s] - %(message)s')
    stream.setFormatter(formatter)
    logger.addHandler(stream)

    if verbosity > 0:
        stream.setLevel(logging.DEBUG)
    else:
        stream.setLevel(logging.INFO)


def _add_arguments():
    parser.add_argument('-v', '--verbosity', action='count', default=0)
    parser.add_argument('input')
    parser.add_argument('output')


def main(args: argparse.Namespace):
    args.input = Path(args.input).expanduser().resolve()
    args.output = Path(args.output).expanduser().resolve()

    with open(args.input, 'r') as file:
        ciphertext = file.read()

    results = {}
    for i in range(1, len(ciphertext)):
        test_text = ciphertext[i:]
        for j, c in enumerate(test_text):
            if c == ciphertext[j]:
                results[i] = results.get(i, 0) + 1

    records = []
    for k in sorted(results.keys()):
        records.append((k, results[k]))
    with open(args.output, 'w') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(('period', 'correlation'))
        writer.writerows(records)
    logger.info('Program complete')


def entry():
    args = parser.parse_args()
    main(args)


if __name__ == '__main__':
    _add_arguments()
    entry()
