from space_repair_assist import SpaceRepairAssist, RepairSession
import json

def test_add_repair_session():
    assist = SpaceRepairAssist()
    assist.add_repair_session(1, "diagnosing")
    assert len(assist.get_repair_sessions()) == 1

def test_approve_tool():
    assist = SpaceRepairAssist()
    assist.add_repair_session(1, "diagnosing")
    assert assist.approve_tool(1, "tool.stl") == True
    assert len(assist.get_approved_tools()) == 1

def test_get_repair_sessions():
    assist = SpaceRepairAssist()
    assist.add_repair_session(1, "diagnosing")
    assist.add_repair_session(2, "guiding")
    sessions = assist.get_repair_sessions()
    assert len(sessions) == 2
    assert sessions[0].status == "diagnosing"
    assert sessions[1].status == "guiding"

def test_get_approved_tools():
    assist = SpaceRepairAssist()
    assist.add_repair_session(1, "diagnosing")
    assist.approve_tool(1, "tool.stl")
    tools = assist.get_approved_tools()
    assert len(tools) == 1
    assert tools[0][0] == 1
    assert tools[0][1] == "tool.stl"

def test_send_to_printer():
    assist = SpaceRepairAssist()
    assist.add_repair_session(1, "diagnosing")
    assist.approve_tool(1, "tool.stl")
    assist.send_to_printer("tool.stl")

def test_reject_tool():
    assist = SpaceRepairAssist()
    assist.add_repair_session(1, "diagnosing")
    assist.approve_tool(1, "tool.stl")
    assert assist.reject_tool(1) == True
    assert assist.get_repair_sessions()[0].tool_file == None

def test_save_to_json():
    assist = SpaceRepairAssist()
    assist.add_repair_session(1, "diagnosing")
    assist.approve_tool(1, "tool.stl")
    assist.save_to_json("test.json")
    with open("test.json", "r") as f:
        data = json.load(f)
        assert len(data["repair_sessions"]) == 1
        assert len(data["approved_tools"]) == 1

def test_load_from_json():
    assist = SpaceRepairAssist()
    assist.add_repair_session(1, "diagnosing")
    assist.approve_tool(1, "tool.stl")
    assist.save_to_json("test.json")
    assist.load_from_json("test.json")
    assert len(assist.get_repair_sessions()) == 1
    assert len(assist.get_approved_tools()) == 1
