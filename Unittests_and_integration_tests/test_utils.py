#!/usr/bin/env python3
"""unittest utils"""

from utils import access_nested_map, get_json, memoize
import unittest
from unittest import TestCase, mock
from unittest.mock import patch, Mock
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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Teste si KeyError est levée pour des chemins invalides.
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Test get_json method """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Test get_json function by simulating an HTTP call with a mock"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        with patch('requests.get', return_value=mock_response):
            real_response = get_json(test_url)
            self.assertEqual(real_response, test_payload)
            mock_response.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """Parameterize and patch"""

    def test_memoize(self):
        """test memoize method"""

        class TestClass:
            """class test in memoize method"""

            def a_method(self):
                """Return result for a_mathod"""
                return 42

            @memoize
            def a_property(self):
                """a_property method in test class"""
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as patched:
            test_class = TestClass()
            real_return = test_class.a_property
            real_return = test_class.a_property

            self.assertEqual(real_return, 42)
            patched.assert_called_once()
