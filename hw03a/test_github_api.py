import unittest
from github_api import get_repositories, get_commit_count, get_github_info


class TestGitHubApi(unittest.TestCase):

    def test_get_repositories(self):
        repos = get_repositories("richkempinski")
        self.assertTrue(len(repos) > 0)

    def test_repository_name_exists(self):
        repos = get_repositories("richkempinski")
        names = [repo["name"] for repo in repos]
        self.assertIn("hellogitworld", names)

    def test_invalid_user(self):
        repos = get_repositories("this_user_should_not_exist_123456789")
        self.assertEqual(repos, [])


if __name__ == "__main__":
    unittest.main()