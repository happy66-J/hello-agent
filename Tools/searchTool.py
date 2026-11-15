import os

from dotenv import load_dotenv
from serpapi import SerpApiClient

def search(query: str)->str:

    print("正在调用搜索工具...")
    try:
        load_dotenv()
        api_key = os.getenv("SERPAPI_API_KEY")
        if not api_key:
            raise Exception("搜索引擎API未配置")
        params = {
            "engine":"google",
            "q": query,
            "api_key": api_key,
            "gl": "cn",
            "hl": "zh-cn",
            }
        client = SerpApiClient(params)
        results = client.get_dict()

        if "answer_box_list" in results:
            return "\n".join(results["answer_box_list"])
        if "answer_box" in results and "answer" in results["answer_box"]:
            return results["answer_box"]["answer"]
        if "knowledge_graph" in results and "description" in results["knowledge_graph"]:
            return results["knowledge_graph"]["description"]
        if "organic_results" in results and results["organic_results"]:
            snippets = [
                f"[{i+1}]{res.get('title','')}\n{res.get('snippet','')}"
                for i, res in enumerate(results["organic_results"][:3])
            ]
            return "\n\n".join(snippets)
        return f"没有关于“{query}”的搜索结果"
    except Exception as e:
        return f"搜索工具调用失败:{e}"
