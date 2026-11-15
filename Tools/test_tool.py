from searchTool import search
from ToolManager import ToolManager
if __name__ == '__main__':
    toolManager = ToolManager()
    des = "一个网页搜索引擎。当你需要回答关于时事、事实以及在你的知识库中找不到的信息时，应使用此工具。"
    toolManager.register_tool("search", des,search)
    print("-----------获取所有可用工具-------------")
    print(toolManager.get_tool_list())
    query = "今天英雄联盟的比赛结果是什么？"
    tool_name="search"
    tool = toolManager.get_tool(tool_name)
    if tool:
        result = tool(query)
        print("----------------搜索结果---------------")
        print(result)
    else:
        print(f"未找到名为{tool_name}的工具")

