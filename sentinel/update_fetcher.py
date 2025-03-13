import requests
from datetime import datetime

class UpdateFetcher:
    def __init__(self):
        self.github_api_url = "https://api.github.com"
        self.headers = {}
        from config import GITHUB_API_TOKEN
        if GITHUB_API_TOKEN:
            self.headers["Authorization"] = f"token {GITHUB_API_TOKEN}"

    def fetch_updates(self, repos):
        updates = []
        for repo in repos:
            repo_updates = self._fetch_repo_updates(repo)
            updates.extend(repo_updates)
        return updates

    def _fetch_repo_updates(self, repo):
        # 获取仓库的最新动态（例如 releases, commits, issues 等）
        url = f"{self.github_api_url}/repos/{repo}/releases"  # 获取 releases 信息
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            releases = response.json()
            return self._parse_releases(repo, releases)
        else:
            print(f"Failed to fetch updates for {repo}: {response.status_code}")
            return []

    def _parse_releases(self, repo, releases):
        # 解析 GitHub API 返回的 releases 数据
        updates = []
        for release in releases:
            update = {
                "repo": repo,
                "type": "release",
                "version": release["tag_name"],
                "created_at": datetime.strptime(release["created_at"], "%Y-%m-%dT%H:%M:%SZ"),
                "author": release["author"]["login"],
                "body": release["body"],
                "url": release["html_url"],
            }
            updates.append(update)
        return updates