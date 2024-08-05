#!/usr/bin/env python3
"""
Parameterize a unit test
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)


if __name__ == '__main__':
    unittest.main()
