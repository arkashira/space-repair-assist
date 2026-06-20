from space_repair_assist import SpaceRepairAssist, ServerRepairScenario

def test_add_scenario():
    assist = SpaceRepairAssist()
    scenario = ServerRepairScenario('example', 'Example scenario', ['step1', 'step2', 'step3'])
    assist.add_scenario(scenario)
    assert len(assist.get_scenarios()) == 1

def test_get_scenarios():
    assist = SpaceRepairAssist()
    scenario1 = ServerRepairScenario('example1', 'Example scenario 1', ['step1', 'step2', 'step3'])
    scenario2 = ServerRepairScenario('example2', 'Example scenario 2', ['step4', 'step5', 'step6'])
    assist.add_scenario(scenario1)
    assist.add_scenario(scenario2)
    scenarios = assist.get_scenarios()
    assert len(scenarios) == 2
    assert scenarios[0].scenario_name == 'example1'
    assert scenarios[1].scenario_name == 'example2'

def test_simulate_repair_found():
    assist = SpaceRepairAssist()
    scenario = ServerRepairScenario('example', 'Example scenario', ['step1', 'step2', 'step3'])
    assist.add_scenario(scenario)
    steps = assist.simulate_repair('example')
    assert steps == ['step1', 'step2', 'step3']

def test_simulate_repair_not_found():
    assist = SpaceRepairAssist()
    scenario = ServerRepairScenario('example', 'Example scenario', ['step1', 'step2', 'step3'])
    assist.add_scenario(scenario)
    steps = assist.simulate_repair('not_found')
    assert steps is None
