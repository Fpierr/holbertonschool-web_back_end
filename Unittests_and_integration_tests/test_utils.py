#!/usr/bin/env python3
"""unittest utils"""

import utils
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Class to testing nested map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test the method returns what it is supposed to """
        self.assertEqual(access_nested_map(nested_map, path), expected)
