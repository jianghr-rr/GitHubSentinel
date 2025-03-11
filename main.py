import time
from sentinel.subscription_manager import SubscriptionManager
from sentinel.update_fetcher import UpdateFetcher
from sentinel.notification_system import NotificationSystem
from sentinel.report_generator import ReportGenerator

def main():
    # 初始化各个模块
    subscription_manager = SubscriptionManager()
    update_fetcher = UpdateFetcher()
    notification_system = NotificationSystem()
    report_generator = ReportGenerator()

    while True:
        # 获取订阅的仓库列表
        repos = subscription_manager.get_subscribed_repos()

        # 获取每个仓库的最新动态
        updates = update_fetcher.fetch_updates(repos)

        # 发送通知
        notification_system.send_notifications(updates)

        # 生成报告
        report_generator.generate_report(updates)

        # 每天执行一次
        time.sleep(86400)

if __name__ == "__main__":
    main()