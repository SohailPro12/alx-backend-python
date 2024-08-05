#!/usr/bin/env python3
"""
Parameterize and patch as decorators
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient
from typing import Dict
from unittest.mock import Mock


class TestGithubOrgClient(unittest.TestCase):
    """
    TestGithubOrgClient class
    """
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch(
        "client.get_json",
    )
    def test_org(
        self,
        org_name: str,
        expected: Dict,
        mock_get_json: Mock
    ) -> None:
        """
        test_org method
        """
        mock_get_json.return_value = expected
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected)
        mock_get_json.assert_called_once()
