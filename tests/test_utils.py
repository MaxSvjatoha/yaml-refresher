import sys
import os

# Add the parent directory to the Python module search path
try:
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
except Exception as e:
    print("Error setting path: {}".format(e))
    print("Continuing anyway...")

# Test functions inside ./utils/utils.py
import utils.utils as utils
import pytest

test_add_two = [
    (1, 2, 3),
    (2, 3, 5),
    (3, 4, 7),
    (4, 5, 9)
]

test_diff_two = [
    (1, 2, -1),
    (2, 3, -1),
    (3, 4, -1),
    (4, 5, -1)
]

test_np_add_two = [
    (1, 2, 3),
    (2, 3, 5),
    (3, 4, 7),
    (4, 5, 9)
]

test_np_diff_two = [
    (1, 2, -1),
    (2, 3, -1),
    (3, 4, -1),
    (4, 5, -1)
]

@pytest.mark.parametrize("a, b, expected", test_add_two)
def test_add_two(a, b, expected):
    assert utils.add_two(a, b) == expected

@pytest.mark.parametrize("a, b, expected", test_diff_two)
def test_diff_two(a, b, expected):
    assert utils.diff_two(a, b) == expected

@pytest.mark.parametrize("a, b, expected", test_np_add_two)
def test_np_add_two(a, b, expected):
    assert utils.np_add_two(a, b) == expected

@pytest.mark.parametrize("a, b, expected", test_np_diff_two)
def test_np_diff_two(a, b, expected):
    assert utils.np_diff_two(a, b) == expected