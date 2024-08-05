#!/usr/bin/env python3
"""
Parameterize a unit test
"""

from parameterized import parameterized
import unittest


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_add(self, name, a, b, expected):
        self.assertEqual(a + b, expected)


if __name__ == '__main__':
    unittest.main()
