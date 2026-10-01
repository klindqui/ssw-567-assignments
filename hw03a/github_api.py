import requests


def get_github_info(user_id):
    repos = get_repositories(user_id)
    results = []

    for repo in repos:
        repo_name = repo["name"]
        commit_count = get_commit_count(user_id, repo_name)
        results.append((repo_name, commit_count))

    return results


def get_repositories(user_id):
    url = f"https://api.github.com/users/{user_id}/repos"
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        return []

    return response.json()


def get_commit_count(user_id, repo_name):
    url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        return 0

    commits = response.json()
    return len(commits)


if __name__ == "__main__":
    results = get_github_info("richkempinski")

    for repo_name, commit_count in results:
        print(f"Repo: {repo_name} Number of commits: {commit_count}")