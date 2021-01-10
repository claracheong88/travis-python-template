"""Some simple tests"""
#simple calculations

from numpy.testing import assert_allclose


def test_addition():
    assert 5 + 4 == 9


def test_subtraction():
    assert 5 - 4 == 1


def test_multiplication():
    assert 5 * 4 == 20


def test_floating_addition():
    assert_allclose(0.1 + 0.2, 0.3)

def test_division():
    assert 10 / 5 == 2

def test_sumproduct():
    assert (5+5)*10 == 100
