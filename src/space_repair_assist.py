import json
from dataclasses import dataclass
from typing import List

@dataclass
class Tool:
    name: str
    description: str

@dataclass
class Part:
    name: str
    description: str

class SpaceRepairAssist:
    def __init__(self):
        self.tools = []
        self.parts = []

    def request_tool(self, tool_name: str, description: str):
        tool = Tool(tool_name, description)
        self.tools.append(tool)
        return tool

    def request_part(self, part_name: str, description: str):
        part = Part(part_name, description)
        self.parts.append(part)
        return part

    def fabricate_tool(self, tool_name: str):
        for tool in self.tools:
            if tool.name == tool_name:
                return tool
        return None

    def fabricate_part(self, part_name: str):
        for part in self.parts:
            if part.name == part_name:
                return part
        return None

    def receive_tool(self, tool_name: str):
        tool = self.fabricate_tool(tool_name)
        if tool:
            return tool
        return None

    def receive_part(self, part_name: str):
        part = self.fabricate_part(part_name)
        if part:
            return part
        return None
