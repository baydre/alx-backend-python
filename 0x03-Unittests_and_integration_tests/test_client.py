#!/usr/bin/env python3
"""Unit tests and integration tests for client.py"""

import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test org method returns correct payload"""
        test_payload = {"payload": True}
        mock_get_json.return_value = test_payload

        client = GithubOrgClient(org_name)
        result = client.org

        self.assertEqual(result, test_payload)
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """Test _public_repos_url returns correct URL"""
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "https://api.github.com/orgs/testorg/repos"}
            client = GithubOrgClient("testorg")
            self.assertEqual(client._public_repos_url, "https://api.github.com/orgs/testorg/repos")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test public_repos returns list of repo names"""
        test_repos = [
            {"name": "repo1"},
            {"name": "repo2"},
        ]
        mock_get_json.return_value = test_repos

        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_url:
            mock_url.return_value = "https://api.github.com/orgs/testorg/repos"
            client = GithubOrgClient("testorg")
            result = client.public_repos()

            self.assertEqual(result, ["repo1", "repo2"])
            mock_get_json.assert_called_once_with("https://api.github.com/orgs/testorg/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has_license returns correct boolean"""
        client = GithubOrgClient("testorg")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)


@patch('client.get_json', return_value=TEST_PAYLOAD[0][0])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Setup once before all tests"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        cls.mock_get.return_value = Mock(**{
            'json.return_value': TEST_PAYLOAD[0][0]
        })

    @classmethod
    def tearDownClass(cls):
        """Cleanup after all tests"""
        cls.get_patcher.stop()

    def test_public_repos(self, mock_get_json):
        """Integration test: public_repos returns correct list"""
        mock_get_json.return_value = TEST_PAYLOAD[0][0]
        client = GithubOrgClient("google")
        repos = client.public_repos()
        expected = [repo["name"] for repo in TEST_PAYLOAD[0][0]]
        self.assertEqual(repos, expected)

    def test_public_repos_with_license(self, mock_get_json):
        """Integration test: public_repos with license filtering"""
        mock_get_json.return_value = TEST_PAYLOAD[0][0]
        client = GithubOrgClient("google")
        repos = client.public_repos(license="apache-2.0")
        expected = [
            repo["name"]
            for repo in TEST_PAYLOAD[0][0]
            if repo.get("license", {}).get("key") == "apache-2.0"
        ]
        self.assertEqual(repos, expected)
