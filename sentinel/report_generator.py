from datetime import datetime

class ReportGenerator:
    def generate_report(self, updates):
        report = self._generate_report_content(updates)
        self._print_report(report)  # 在命令行中显示报告
        self._save_report(report)   # 保存报告到文件

    def _generate_report_content(self, updates):
        # 生成报告内容
        report = f"GitHub Sentinel Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        for update in updates:
            report += f"Repo: {update['repo']}\n"
            report += f"Type: {update['type']}\n"
            report += f"Version: {update['version']}\n"
            report += f"Created At: {update['created_at']}\n"
            report += f"Author: {update['author']}\n"
            report += f"Details: {update['body']}\n"
            report += f"URL: {update['url']}\n\n"
        return report

    def _print_report(self, report):
        # 在命令行中显示报告
        print(report)

    def _save_report(self, report):
        # 保存报告到文件
        with open("github_sentinel_report.txt", "w") as f:
            f.write(report)
        print("Report saved to github_sentinel_report.txt")