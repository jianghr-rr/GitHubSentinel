import threading
import time
from sentinel.subscription_manager import SubscriptionManager
from sentinel.update_fetcher import UpdateFetcher
from sentinel.notification_system import NotificationSystem
from sentinel.report_generator import ReportGenerator

def scheduler_task(subscription_manager, update_fetcher, notification_system, report_generator):
    """后台定时任务，定期获取更新并生成报告"""
    while True:
        repos = subscription_manager.get_subscribed_repos()
        updates = update_fetcher.fetch_updates(repos)
        notification_system.send_notifications(updates)
        report_generator.generate_report(updates)  # 生成报告并显示在命令行中
        time.sleep(86400)  # 每天执行一次

def main():
    # 初始化各个模块
    subscription_manager = SubscriptionManager()
    update_fetcher = UpdateFetcher()
    notification_system = NotificationSystem()
    report_generator = ReportGenerator()

    # 启动后台定时任务
    scheduler_thread = threading.Thread(
        target=scheduler_task,
        args=(subscription_manager, update_fetcher, notification_system, report_generator),
        daemon=True  # 设置为守护线程，主程序退出时自动结束
    )
    scheduler_thread.start()

    # 交互式循环
    while True:
        print("\nGitHub Sentinel - 交互式工具")
        print("1. 查看当前订阅的仓库")
        print("2. 增加订阅")
        print("3. 移除订阅")
        print("4. 立即获取更新")
        print("5. 退出")
        choice = input("请输入选项: ")

        if choice == "1":
            # 查看当前订阅的仓库
            repos = subscription_manager.get_subscribed_repos()
            print("\n当前订阅的仓库:")
            for repo in repos:
                print(f"- {repo}")
        elif choice == "2":
            # 增加订阅
            repo = input("请输入要订阅的仓库（格式：owner/repo）: ")
            subscription_manager.add_subscription(repo)
            print(f"已增加订阅: {repo}")
        elif choice == "3":
            # 移除订阅
            repo = input("请输入要移除的仓库（格式：owner/repo）: ")
            subscription_manager.remove_subscription(repo)
            print(f"已移除订阅: {repo}")
        elif choice == "4":
            # 立即获取更新
            repos = subscription_manager.get_subscribed_repos()
            updates = update_fetcher.fetch_updates(repos)
            notification_system.send_notifications(updates)
            report_generator.generate_report(updates)  # 生成报告并显示在命令行中
        elif choice == "5":
            # 退出
            print("退出 GitHub Sentinel。")
            break
        else:
            print("无效选项，请重新输入。")

if __name__ == "__main__":
    main()