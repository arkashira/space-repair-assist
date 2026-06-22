import json
from dataclasses import dataclass
from typing import List

@dataclass
class ToolOrPart:
    name: str
    description: str

class SpaceRepairAssist:
    def __init__(self):
        self.requests = []
        self.fabricated_tools_or_parts = []

    def receive_request(self, tool_or_part: ToolOrPart):
        self.requests.append(tool_or_part)

    def fabricate(self, tool_or_part: ToolOrPart):
        # Simulate 3D printing fabrication
        self.fabricated_tools_or_parts.append(tool_or_part)

    def get_fabricated_tools_or_parts(self) -> List[ToolOrPart]:
        return self.fabricated_tools_or_parts

    def process_requests(self):
        for request in self.requests:
            self.fabricate(request)

def main():
    assist = SpaceRepairAssist()
    tool = ToolOrPart("Wrench", "A tool for tightening bolts")
    assist.receive_request(tool)
    assist.process_requests()
    fabricated_tools = assist.get_fabricated_tools_or_parts()
    print(json.dumps([tool.__dict__ for tool in fabricated_tools]))

if __name__ == "__main__":
    main()
