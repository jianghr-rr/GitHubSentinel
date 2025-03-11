# 更新获取器
import requests
from datetime import datetime

class UpdateFetcher:
    def __init__(self):
        self.github_api_url = "https://api.github.com"

    def fetch_updates(self, repos):
        updates = []
        for repo in repos:
            repo_updates = self._fetch_repo_updates(repo)
            updates.extend(repo_updates)
        return updates

    def _fetch_repo_updates(self, repo):
        # 获取仓库的最新动态，例如 commits, issues, pull requests 等
        url = f"{self.github_api_url}/repos/{repo}/events"
        response = requests.get(url)
        if response.status_code == 200:
            events = response.json()
            return self._parse_events(events)
        else:
            return []

    def _parse_events(self, events):
        # 解析 GitHub API 返回的事件数据
        updates = []
        for event in events:
            update = {
                "repo": event["repo"]["name"],
                "type": event["type"],
                "created_at": datetime.strptime(event["created_at"], "%Y-%m-%dT%H:%M:%SZ"),
                "payload": event["payload"]
            }
            updates.append(update)
        return updates