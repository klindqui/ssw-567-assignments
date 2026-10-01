import unittest
from unittest.mock import patch, Mock
from github_api import get_repositories, get_commit_count, get_github_info


class TestGitHubApi(unittest.TestCase):

    @patch("github_api.requests.get")
    def test_get_repositories(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"name": "Repo1"},
            {"name": "Repo2"}
        ]
        mock_get.return_value = mock_response

        repos = get_repositories("testuser")

        self.assertEqual(len(repos), 2)
        self.assertEqual(repos[0]["name"], "Repo1")
        self.assertEqual(repos[1]["name"], "Repo2")

    @patch("github_api.requests.get")
    def test_get_commit_count(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"sha": "commit1"},
            {"sha": "commit2"},
            {"sha": "commit3"}
        ]
        mock_get.return_value = mock_response

        count = get_commit_count("testuser", "Repo1")

        self.assertEqual(count, 3)

    @patch("github_api.requests.get")
    def test_get_github_info(self, mock_get):
        repo_response = Mock()
        repo_response.status_code = 200
        repo_response.json.return_value = [
            {"name": "Repo1"},
            {"name": "Repo2"}
        ]

        repo1_commits = Mock()
        repo1_commits.status_code = 200
        repo1_commits.json.return_value = [
            {"sha": "commit1"},
            {"sha": "commit2"}
        ]

        repo2_commits = Mock()
        repo2_commits.status_code = 200
        repo2_commits.json.return_value = [
            {"sha": "commit1"},
            {"sha": "commit2"},
            {"sha": "commit3"}
        ]

        mock_get.side_effect = [
            repo_response,
            repo1_commits,
            repo2_commits
        ]

        results = get_github_info("testuser")

        self.assertEqual(results, [
            ("Repo1", 2),
            ("Repo2", 3)
        ])

    @patch("github_api.requests.get")
    def test_invalid_user(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        repos = get_repositories("invaliduser")

        self.assertEqual(repos, [])


if __name__ == "__main__":
    unittest.main()