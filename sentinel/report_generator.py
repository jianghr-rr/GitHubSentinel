from datetime import datetime
import os
from sentinel.llm import LLM

class ReportGenerator:
    def __init__(self):
        self.llm = LLM()  # 初始化 LLM 模块

    def generate_daily_progress(self, updates, date_str=None):
        """
        生成每日进展 Markdown 文件
        """
        # 如果没有提供日期，则使用当前日期
        if date_str is None:
            date_str = datetime.now().strftime("%Y-%m-%d")

        # 按仓库分组
        repo_updates = {}
        for update in updates:
            repo = update["repo"]
            if repo not in repo_updates:
                repo_updates[repo] = []
            repo_updates[repo].append(update)

        # 为每个仓库生成 Markdown 文件
        for repo, updates in repo_updates.items():
            self._generate_repo_daily_progress(repo, updates, date_str)

    def _generate_repo_daily_progress(self, repo, updates, date_str):
        """
        为单个仓库生成每日进展 Markdown 文件
        """
        # 生成文件名
        filename = f"{repo.replace('/', '_')}_{date_str}.md"
        os.makedirs("daily_progress", exist_ok=True)
        filepath = os.path.join("daily_progress", filename)

        # 生成 Markdown 内容
        content = f"# {repo} 每日进展 - {date_str}\n\n"
        if not updates:
            content += "今日没有新的更新。\n"
        else:
            for update in updates:
                if update['type'] == 'release':
                    title = update.get('name', 'Untitled Release')
                elif update['type'] == 'commit':
                    title = update.get('message', 'Untitled Commit')
                else:
                    title = update.get('title', 'Untitled')

                content += f"## {update['type'].capitalize()}: {title}\n"
                content += f"- **作者**: {update['author']}\n"
                content += f"- **创建时间**: {update['created_at']}\n"
                if update['type'] != 'commit':
                    content += f"- **详情**: {update['body']}\n"
                content += f"- **链接**: [{update['url']}]({update['url']})\n\n"

        # 保存文件
        with open(filepath, "w") as f:
            f.write(content)
        print(f"Daily progress saved to {filepath}")

    def generate_daily_report(self, repo, date_str):
        """
        生成每日报告 Markdown 文件
        """
        # 读取每日进展文件
        filename = f"{repo.replace('/', '_')}_{date_str}.md"
        filepath = os.path.join("daily_progress", filename)

        if not os.path.exists(filepath):
            print(f"No daily progress found for {repo} on {date_str}")
            return

        with open(filepath, "r") as f:
            content = f.read()

        # 调用 LLM 生成总结
        summary = self.llm.summarize_daily_progress(content)

        # 保存每日报告
        report_filename = f"{repo.replace('/', '_')}_{date_str}_report.md"
        report_filepath = os.path.join("daily_reports", report_filename)
        os.makedirs("daily_reports", exist_ok=True)

        with open(report_filepath, "w") as f:
            f.write(summary)
        print(f"Daily report saved to {report_filepath}")