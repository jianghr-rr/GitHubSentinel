# 报告生成器
from datetime import datetime

class ReportGenerator:
    def generate_report(self, updates):
        report = self._generate_report_content(updates)
        self._save_report(report)

    def _generate_report_content(self, updates):
        # 生成报告内容
        report = f"GitHub Sentinel Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        for update in updates:
            report += f"Repo: {update['repo']}\n"
            report += f"Type: {update['type']}\n"
            report += f"Created At: {update['created_at']}\n"
            report += f"Payload: {update['payload']}\n\n"
        return report

    def _save_report(self, report):
        # 保存报告到文件或发送到指定位置
        with open("github_sentinel_report.txt", "w") as f:
            f.write(report)