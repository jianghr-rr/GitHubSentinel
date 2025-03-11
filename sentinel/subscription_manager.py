# 订阅管理器
class SubscriptionManager:
    def __init__(self):
        self.subscriptions = self._load_subscriptions()

    def _load_subscriptions(self):
        # 从配置文件或数据库中加载订阅的仓库列表
        # 这里假设从 config.py 中加载
        from config import SUBSCRIBED_REPOS
        return SUBSCRIBED_REPOS

    def get_subscribed_repos(self):
        return self.subscriptions

    def add_subscription(self, repo):
        self.subscriptions.append(repo)
        self._save_subscriptions()

    def remove_subscription(self, repo):
        self.subscriptions.remove(repo)
        self._save_subscriptions()

    def _save_subscriptions(self):
        # 将订阅的仓库列表保存到配置文件或数据库中
        pass