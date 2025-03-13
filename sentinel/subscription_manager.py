import json
import os
from config import SUBSCRIBED_REPOS

class SubscriptionManager:
    def __init__(self):
        self.subscriptions_file = "subscriptions.json"  # 订阅列表保存的文件
        self.subscriptions = self._load_subscriptions()

    def _load_subscriptions(self):
        # 从文件中加载订阅的仓库列表
        if os.path.exists(self.subscriptions_file):
            with open(self.subscriptions_file, "r") as f:
                return json.load(f)
        else:
            # 如果文件不存在，使用 config.py 中的默认值
            return SUBSCRIBED_REPOS.copy()  # 使用 copy() 避免直接修改原列表

    def get_subscribed_repos(self):
        return self.subscriptions

    def add_subscription(self, repo):
        if repo not in self.subscriptions:
            self.subscriptions.append(repo)
            self._save_subscriptions()

    def remove_subscription(self, repo):
        if repo in self.subscriptions:
            self.subscriptions.remove(repo)
            self._save_subscriptions()

    def _save_subscriptions(self):
        # 将订阅的仓库列表保存到文件中
        with open(self.subscriptions_file, "w") as f:
            json.dump(self.subscriptions, f)