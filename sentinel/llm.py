from openai import OpenAI
from config import OPENAI_API_KEY, OPENAI_API_BASE_URL

class LLM:
    def __init__(self):
        # 初始化 OpenAI 客户端
        self.client = OpenAI(
            api_key=OPENAI_API_KEY,
            base_url=OPENAI_API_BASE_URL,  # 设置自定义 API 端点
        )

    def summarize_daily_progress(self, content):
        # 调用 GPT-4 API 生成总结
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "你是一个技术助手，负责整理 GitHub 项目的每日进展。"},
                {"role": "user", "content": f"请整理以下 GitHub 项目的每日进展，并生成一份正式的报告：\n\n{content}"},
            ],
            max_tokens=1000,
        )
        return response.choices[0].message.content