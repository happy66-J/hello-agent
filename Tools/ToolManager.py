from typing import Dict, Any, Callable


class ToolManager:
    def __init__(self):
        self.tool_list:Dict[str, Dict[str, Any]] = {}

    def register_tool(self, name: str, description: str, func: Callable):
        """注册工具"""
        if name in self.tool_list:
            print(f"{name}工具已存在，将被覆盖")
        self.tool_list[name] = {"description": description, "func": func}
        print(f"{name}工具已注册")

    def get_tool(self, name: str) -> Callable|None:
        """根据名称获取工具"""
        return self.tool_list.get(name,{}).get("func")

    def get_tool_list(self) -> str:
        """获取所有可用工具"""
        des =[
            f"-{name}: {info['description']}"
            for name, info in self.tool_list.items()
        ]
        return "\n".join(des)
