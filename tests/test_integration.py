#!/usr/bin/env python3
# coding=utf-8

import argparse
from pathlib import Path

import pytest

import autocorrelationcalc.__main__ as main


@pytest.fixture()
def args(tmp_path: Path) -> argparse.Namespace:
    args = argparse.Namespace()
    args.verbosity = 0
    args.input = './resources/cipher_1.txt'
    args.output = Path(tmp_path, 'output.csv')
    return args


def test_integration(args: argparse.Namespace):
    main.main(args)
