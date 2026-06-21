from space_repair_assist import SpaceRepairAssist, RepairSession

def test_add_session():
    assist = SpaceRepairAssist()
    session = RepairSession(1, "diagnosing")
    assist.add_session(session)
    assert len(assist.list_sessions()) == 1

def test_list_sessions():
    assist = SpaceRepairAssist()
    session1 = RepairSession(1, "diagnosing")
    session2 = RepairSession(2, "guiding")
    assist.add_session(session1)
    assist.add_session(session2)
    sessions = assist.list_sessions()
    assert len(sessions) == 2
    assert sessions[0].id == 1
    assert sessions[1].id == 2

def test_approve_tool():
    assist = SpaceRepairAssist()
    session = RepairSession(1, "diagnosing")
    assist.add_session(session)
    result = assist.approve_tool(1)
    assert result.startswith("Tool approved")

def test_reject_tool():
    assist = SpaceRepairAssist()
    session = RepairSession(1, "diagnosing")
    assist.add_session(session)
    result = assist.reject_tool(1)
    assert result.startswith("Tool rejected")

def test_send_to_printer():
    assist = SpaceRepairAssist()
    session = RepairSession(1, "diagnosing")
    assist.add_session(session)
    assist.approve_tool(1)
    printed_tools = assist.send_to_printer()
    assert len(printed_tools) == 1
    assert printed_tools[0] == "tool_1.stl"

def test_session_not_found():
    assist = SpaceRepairAssist()
    result = assist.approve_tool(1)
    assert result == "Session not found"
