import json
from dataclasses import dataclass
from datetime import datetime

@dataclass
class RepairSession:
    id: int
    status: str
    tool_file: str = None

class SpaceRepairAssist:
    def __init__(self):
        self.repair_sessions = []
        self.approved_tools = []

    def add_repair_session(self, id, status):
        self.repair_sessions.append(RepairSession(id, status))

    def approve_tool(self, session_id, tool_file):
        for session in self.repair_sessions:
            if session.id == session_id:
                session.tool_file = tool_file
                self.approved_tools.append((session_id, tool_file, datetime.now().timestamp()))
                return True
        return False

    def get_repair_sessions(self):
        return self.repair_sessions

    def get_approved_tools(self):
        return self.approved_tools

    def send_to_printer(self, tool_file):
        # Simulate sending to printer
        print(f"Sending {tool_file} to printer")

    def reject_tool(self, session_id):
        for session in self.repair_sessions:
            if session.id == session_id and session.tool_file:
                session.tool_file = None
                return True
        return False

    def save_to_json(self, filename):
        data = {
            "repair_sessions": [{"id": session.id, "status": session.status, "tool_file": session.tool_file} for session in self.repair_sessions],
            "approved_tools": self.approved_tools
        }
        with open(filename, "w") as f:
            json.dump(data, f)

    def load_from_json(self, filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.repair_sessions = [RepairSession(session["id"], session["status"], session["tool_file"]) for session in data["repair_sessions"]]
                self.approved_tools = data["approved_tools"]
        except FileNotFoundError:
            pass
