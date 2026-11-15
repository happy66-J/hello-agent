import os
from dotenv import load_dotenv
from typing import List, Dict
from openai import OpenAI

class HelloAgent:
    def __init__(self, default_model:str|None = None, api_key:str|None = None, base_url:str|None = None, timeout:int = 60):
        """初始化客户端，优先使用传入参数配置，默认使用env配置"""
        load_dotenv()
        self.llm_api_key = api_key or os.getenv("DEEPSEEK_API_KEY")
        self.llm_base_url = base_url or os.getenv("LLM_BASE_URL")
        self.llm_base_model = default_model or os.getenv("LLM_DEFAULT_MODEL")

        if not all([self.llm_api_key, self.llm_base_url, self.llm_base_model]):
            raise ValueError("llm信息请在.env文件中补充完整")

        self.agent = OpenAI(api_key=self.llm_api_key, base_url=self.llm_base_url, timeout=timeout)

    def think(self,message:List[Dict[str,str]], temperature: float | None = None) -> str|None:

        print("大模型输出生成中...")
        try:
            llm_response = self.agent.chat.completions.create(messages=message, temperature=temperature, model=self.llm_base_model, stream=True)
            content_list = []
            for chunk in llm_response:
                if not chunk.choices:
                    continue
                content = chunk.choices[0].delta.content or ""
                print(content, end="", flush=True)
                content_list.append(content)
        except Exception as e:
            print(f"回答生成失败:{e}")
            return None

        return "".join(content_list)

if __name__ == '__main__':
    agent = HelloAgent()
    message = [{"role":"system","content":"你是我的助手，名字叫冬瓜"},
               {"role":"user","content":"你有联网搜索功能吗，比如今天英雄联盟比赛的结果是什么"}]
    try:
        res = agent.think(message=message)
        if res is not None:
            print("输出成功")
    except Exception as e:
        print(e)