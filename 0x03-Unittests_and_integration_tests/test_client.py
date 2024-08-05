#!/usr/bin/env python3
"""
Parameterize and patch as decorators
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient
from typing import Dict
from unittest.mock import Mock, PropertyMock


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

    def test_public_repos_url(self) -> None:
        """Tests the `_public_repos_url` property."""
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )
