import json
from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class RepairSession:
    id: int
    status: str
    tool_file: str = None
    approved: bool = False

class SpaceRepairAssist:
    def __init__(self):
        self.sessions = []
        self.approved_tools = []

    def add_session(self, session: RepairSession):
        self.sessions.append(session)

    def list_sessions(self):
        return self.sessions

    def approve_tool(self, session_id: int):
        for session in self.sessions:
            if session.id == session_id:
                session.approved = True
                session.tool_file = f"tool_{session_id}.stl"
                self.approved_tools.append(session.tool_file)
                return f"Tool approved for session {session_id} at {datetime.now()}"
        return "Session not found"

    def reject_tool(self, session_id: int):
        for session in self.sessions:
            if session.id == session_id:
                session.approved = False
                return f"Tool rejected for session {session_id} at {datetime.now()}"
        return "Session not found"

    def send_to_printer(self):
        printed_tools = []
        for tool in self.approved_tools:
            printed_tools.append(tool)
            print(f"Sending {tool} to printer")
        return printed_tools
