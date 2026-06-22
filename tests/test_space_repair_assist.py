from space_repair_assist import SpaceRepairAssist, ToolOrPart

def test_receive_request():
    assist = SpaceRepairAssist()
    tool = ToolOrPart("Wrench", "A tool for tightening bolts")
    assist.receive_request(tool)
    assert len(assist.requests) == 1
    assert assist.requests[0].name == "Wrench"

def test_fabricate():
    assist = SpaceRepairAssist()
    tool = ToolOrPart("Wrench", "A tool for tightening bolts")
    assist.fabricate(tool)
    assert len(assist.fabricated_tools_or_parts) == 1
    assert assist.fabricated_tools_or_parts[0].name == "Wrench"

def test_process_requests():
    assist = SpaceRepairAssist()
    tool1 = ToolOrPart("Wrench", "A tool for tightening bolts")
    tool2 = ToolOrPart("Pliers", "A tool for gripping objects")
    assist.receive_request(tool1)
    assist.receive_request(tool2)
    assist.process_requests()
    assert len(assist.fabricated_tools_or_parts) == 2
    assert assist.fabricated_tools_or_parts[0].name == "Wrench"
    assert assist.fabricated_tools_or_parts[1].name == "Pliers"

def test_get_fabricated_tools_or_parts():
    assist = SpaceRepairAssist()
    tool = ToolOrPart("Wrench", "A tool for tightening bolts")
    assist.fabricate(tool)
    fabricated_tools = assist.get_fabricated_tools_or_parts()
    assert len(fabricated_tools) == 1
    assert fabricated_tools[0].name == "Wrench"

def test_edge_case_empty_request():
    assist = SpaceRepairAssist()
    assist.process_requests()
    assert len(assist.fabricated_tools_or_parts) == 0
