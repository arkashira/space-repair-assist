from space_repair_assist import SpaceRepairAssist, Tool, Part

def test_request_tool():
    assist = SpaceRepairAssist()
    tool = assist.request_tool("Wrench", "A tool for tightening bolts")
    assert tool.name == "Wrench"
    assert tool.description == "A tool for tightening bolts"

def test_request_part():
    assist = SpaceRepairAssist()
    part = assist.request_part("Bolt", "A part for holding things together")
    assert part.name == "Bolt"
    assert part.description == "A part for holding things together"

def test_fabricate_tool():
    assist = SpaceRepairAssist()
    tool = assist.request_tool("Wrench", "A tool for tightening bolts")
    fabricated_tool = assist.fabricate_tool("Wrench")
    assert fabricated_tool.name == "Wrench"
    assert fabricated_tool.description == "A tool for tightening bolts"

def test_fabricate_part():
    assist = SpaceRepairAssist()
    part = assist.request_part("Bolt", "A part for holding things together")
    fabricated_part = assist.fabricate_part("Bolt")
    assert fabricated_part.name == "Bolt"
    assert fabricated_part.description == "A part for holding things together"

def test_receive_tool():
    assist = SpaceRepairAssist()
    tool = assist.request_tool("Wrench", "A tool for tightening bolts")
    received_tool = assist.receive_tool("Wrench")
    assert received_tool.name == "Wrench"
    assert received_tool.description == "A tool for tightening bolts"

def test_receive_part():
    assist = SpaceRepairAssist()
    part = assist.request_part("Bolt", "A part for holding things together")
    received_part = assist.receive_part("Bolt")
    assert received_part.name == "Bolt"
    assert received_part.description == "A part for holding things together"

def test_receive_non_existent_tool():
    assist = SpaceRepairAssist()
    received_tool = assist.receive_tool("NonExistentTool")
    assert received_tool is None

def test_receive_non_existent_part():
    assist = SpaceRepairAssist()
    received_part = assist.receive_part("NonExistentPart")
    assert received_part is None
