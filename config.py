from dotenv import load_dotenv
import os

# 加载 .env 文件
load_dotenv()

# 订阅的 GitHub 仓库列表
SUBSCRIBED_REPOS = [
    "facebook/react",  # 示例仓库
]

# 通知方式（暂时留空，后续实现）
NOTIFICATION_METHODS = []

# GitHub API 令牌（从 .env 文件中读取）
GITHUB_API_TOKEN = os.getenv("GITHUB_API_TOKEN")