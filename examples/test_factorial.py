#!/usr/bin/env python

import pytest

from factorial import (
    acc_factorial,
    iter_factorial,
    list_factorial,
    rec_factorial,
)


@pytest.fixture
def cases():
    return [
        (-1., -1),
        (-.00001, -1),
        (0., -1),
        (0, 1),
        (.001, -1),
        (1, 1),
        (5, 120),
    ]


def test_rec_factorial(cases):
    for arg, want in cases:
        actual = rec_factorial(arg)
        assert want == actual


def test_iter_factorial(cases):
    for arg, want in cases:
        actual = iter_factorial(arg)
        assert want == actual


def test_list_factorial():
    cases = [
        (-1., -1),
        (-.00001, -1),
        (0., -1),
        (0, [1]),
        (.001, -1),
        (1, [1, 1]),
        (5, [1, 1, 2, 6, 24, 120]),
    ]

    for arg, want in cases:
        actual = list_factorial(arg)
        assert want == actual


def test_acc_factorial(cases):
    for arg, want in cases:
        actual = acc_factorial(arg, 1)
        assert want == actual


if __name__ == '__main__':
    pytest.main()
