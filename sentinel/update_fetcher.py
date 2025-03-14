import requests
from datetime import datetime
from config import GITHUB_API_TOKEN

class UpdateFetcher:
    def __init__(self):
        self.github_api_url = "https://api.github.com"
        self.headers = {}
        if GITHUB_API_TOKEN:
            self.headers["Authorization"] = f"token {GITHUB_API_TOKEN}"

    def fetch_updates(self, repos):
        updates = []
        for repo in repos:
            repo_updates = self._fetch_repo_updates(repo)
            updates.extend(repo_updates)
        return updates

    def _fetch_repo_updates(self, repo):
        # 获取仓库的最新动态（例如 releases, commits, issues, pull requests 等）
        updates = []
        updates.extend(self._fetch_repo_releases(repo))
        updates.extend(self._fetch_repo_commits(repo))
        updates.extend(self._fetch_repo_issues(repo))
        updates.extend(self._fetch_repo_pull_requests(repo))
        return updates

    def _fetch_repo_releases(self, repo):
        # 获取仓库的 releases
        url = f"{self.github_api_url}/repos/{repo}/releases"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            releases = response.json()
            return self._parse_releases(repo, releases)
        else:
            print(f"Failed to fetch releases for {repo}: {response.status_code}")
            return []

    def _fetch_repo_commits(self, repo):
        # 获取仓库的 commits
        url = f"{self.github_api_url}/repos/{repo}/commits"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            commits = response.json()
            return self._parse_commits(repo, commits)
        else:
            print(f"Failed to fetch commits for {repo}: {response.status_code}")
            return []

    def _fetch_repo_issues(self, repo):
        # 获取仓库的 issues
        url = f"{self.github_api_url}/repos/{repo}/issues"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            issues = response.json()
            return self._parse_issues(repo, issues)
        else:
            print(f"Failed to fetch issues for {repo}: {response.status_code}")
            return []

    def _fetch_repo_pull_requests(self, repo):
        # 获取仓库的 pull requests
        url = f"{self.github_api_url}/repos/{repo}/pulls"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            pull_requests = response.json()
            return self._parse_pull_requests(repo, pull_requests)
        else:
            print(f"Failed to fetch pull requests for {repo}: {response.status_code}")
            return []

    def _parse_releases(self, repo, releases):
        # 解析 releases
        updates = []
        for release in releases:
            update = {
                "repo": repo,
                "type": "release",
                "name": release.get("name", "Untitled Release"),
                "created_at": datetime.strptime(release["created_at"], "%Y-%m-%dT%H:%M:%SZ"),
                "author": release["author"]["login"],
                "body": release["body"],
                "url": release["html_url"],
            }
            updates.append(update)
        return updates

    def _parse_commits(self, repo, commits):
        # 解析 commits
        updates = []
        for commit in commits:
            update = {
                "repo": repo,
                "type": "commit",
                "message": commit["commit"]["message"],
                "created_at": datetime.strptime(commit["commit"]["author"]["date"], "%Y-%m-%dT%H:%M:%SZ"),
                "author": commit["commit"]["author"]["name"],
                "url": commit["html_url"],
            }
            updates.append(update)
        return updates

    def _parse_issues(self, repo, issues):
        # 解析 issues
        updates = []
        for issue in issues:
            update = {
                "repo": repo,
                "type": "issue",
                "title": issue.get("title", "Untitled"),
                "created_at": datetime.strptime(issue["created_at"], "%Y-%m-%dT%H:%M:%SZ"),
                "author": issue["user"]["login"],
                "body": issue["body"],
                "url": issue["html_url"],
            }
            updates.append(update)
        return updates

    def _parse_pull_requests(self, repo, pull_requests):
        # 解析 pull requests
        updates = []
        for pr in pull_requests:
            update = {
                "repo": repo,
                "type": "pull_request",
                "title": pr.get("title", "Untitled"),
                "created_at": datetime.strptime(pr["created_at"], "%Y-%m-%dT%H:%M:%SZ"),
                "author": pr["user"]["login"],
                "body": pr["body"],
                "url": pr["html_url"],
            }
            updates.append(update)
        return updates