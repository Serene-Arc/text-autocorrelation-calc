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
    parser.add_argument('inputs', nargs='+')


def main(args: argparse.Namespace):
    _setup_logging(args.verbosity)
    args.inputs = [Path(a).expanduser().resolve() for a in args.inputs]

    for p in args.inputs:
        with open(p, 'r') as file:
            ciphertext = file.read()

        ciphertext = ciphertext.lower().replace(' ', '')
        logger.debug('Beginning calculation')
        results = {}
        for i in range(1, len(ciphertext)):
            test_text = ciphertext[i:]
            count = sum([test_text[k] == ciphertext[k] for k in range(0, len(test_text))])
            correlation = count / len(test_text)
            results[i] = correlation

        records = []
        for k in sorted(results.keys()):
            records.append((k, results[k]))
        out_path = Path(p.name + '_autocorrelation.csv')
        with open(out_path, 'w') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(('period', 'correlation'))
            writer.writerows(records)
        logger.info(f'File written to {out_path}')


def entry():
    args = parser.parse_args()
    main(args)


if __name__ == '__main__':
    _add_arguments()
    entry()
