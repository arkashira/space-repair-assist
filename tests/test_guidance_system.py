import pytest
from guidance_system import GuidanceSystem, RepairStep, RepairStepStatus

def test_get_current_step():
    steps = [RepairStep("Step 1"), RepairStep("Step 2")]
    system = GuidanceSystem(steps)
    assert system.get_current_step().description == "Step 1"

def test_mark_step_as_completed():
    steps = [RepairStep("Step 1"), RepairStep("Step 2")]
    system = GuidanceSystem(steps)
    system.mark_step_as_completed()
    assert system.get_current_step().description == "Step 2"

def test_get_progress():
    steps = [RepairStep("Step 1", RepairStepStatus.COMPLETED), RepairStep("Step 2")]
    system = GuidanceSystem(steps)
    assert system.get_progress() == 0.5

def test_provide_feedback():
    steps = [RepairStep("Step 1", RepairStepStatus.COMPLETED), RepairStep("Step 2", RepairStepStatus.COMPLETED)]
    system = GuidanceSystem(steps)
    assert system.provide_feedback() == "Repair completed successfully"

def test_provide_feedback_incomplete():
    steps = [RepairStep("Step 1", RepairStepStatus.COMPLETED), RepairStep("Step 2")]
    system = GuidanceSystem(steps)
    assert system.provide_feedback() == "Please complete the remaining steps"

def test_mark_step_as_completed_all_completed():
    steps = [RepairStep("Step 1", RepairStepStatus.COMPLETED), RepairStep("Step 2", RepairStepStatus.COMPLETED)]
    system = GuidanceSystem(steps)
    with pytest.raises(ValueError):
        system.mark_step_as_completed()
