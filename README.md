# GitHub Sentinel

GitHub Sentinel 是一款开源工具类 AI Agent，专为开发者和项目管理人员设计，能够定期（每日/每周）自动获取并汇总订阅的 GitHub 仓库最新动态。其主要功能包括订阅管理、更新获取、通知系统、报告生成。通过及时获取和推送最新的仓库更新，GitHub Sentinel 大大提高了团队协作效率和项目管理的便捷性，使用户能够更高效地跟踪项目进展，快速响应和处理变更，确保项目始终处于最新状态。

---

## 功能

- **订阅管理**：轻松管理订阅的 GitHub 仓库列表。
- **更新获取**：定期从 GitHub API 获取仓库的最新动态（如 `commits`、`issues`、`pull requests`、`releases`）。
- **每日进展**：生成每日进展 Markdown 文件，汇总订阅仓库的更新。
- **每日报告**：调用 GPT-4 或 GPT-3.5-turbo 生成每日报告，整理汇总 `commits`、`issues` 和 `pull requests` 信息。
- **通知系统**：支持通过邮件、Slack 等方式发送更新通知（待实现）。
- **交互式工具**：提供命令行交互界面，支持动态增加或移除订阅、立即获取更新、生成报告等操作。

---

## 安装

### 1. 克隆仓库

```bash
git clone https://github.com/yourusername/github-sentinel.git
cd github-sentinel
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3.配置环境变量

在项目根目录下创建 .env 文件，并填写以下内容：

```bash
GITHUB_API_TOKEN=your_github_token_here
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_API_BASE_URL=  # 如果使用 OpenAI 官方服务，可以留空
```

---

## 使用

### 1. 运行程序

```bash
python main.py
```

### 2. 交互式菜单

程序启动后，会显示以下菜单：

```bash
GitHub Sentinel - 交互式工具
1. 查看当前订阅的仓库
2. 增加订阅
3. 移除订阅
4. 立即获取更新
5. 生成每日报告
6. 退出
请输入选项:
```
选项 1：查看当前订阅的仓库。

选项 2：增加订阅的仓库（格式：owner/repo）。

选项 3：移除订阅的仓库（格式：owner/repo）。

选项 4：立即获取订阅仓库的最新动态，并生成每日进展文件。

选项 5：生成指定仓库的每日报告。

选项 6：退出程序。

### 3. 查看生成的文件

每日进展文件：位于 daily_progress/ 目录下，文件名为 {repo}_{date}.md。
每日报告文件：位于 daily_reports/ 目录下，文件名为 {repo}_{date}_report.md。

## 配置

### 1. 订阅管理

默认订阅的仓库列表在 config.py 中定义：

```python
SUBSCRIBED_REPOS = [
    "facebook/react",  # 示例仓库
]
```
可以通过交互式菜单动态增加或移除订阅。

## 示例

### 1. 增加订阅

请输入选项: 2
请输入要订阅的仓库（格式：owner/repo）: langchain-ai/langchain
已增加订阅: langchain-ai/langchain
2. 立即获取更新
复制
请输入选项: 4
Daily progress saved to daily_progress/facebook_react_2023-10-25.md
Daily progress saved to daily_progress/langchain-ai_langchain_2023-10-25.md
3. 生成每日报告
复制
请输入选项: 5
请输入要生成报告的仓库（格式：owner/repo）: facebook/react
请输入日期（格式：YYYY-MM-DD）: 2023-10-25
Daily report saved to daily_reports/facebook_react_2023-10-25_report.md
