import json
from dataclasses import dataclass
from enum import Enum

class RepairStepStatus(Enum):
    NOT_STARTED = 1
    IN_PROGRESS = 2
    COMPLETED = 3

@dataclass
class RepairStep:
    description: str
    status: RepairStepStatus = RepairStepStatus.NOT_STARTED

class GuidanceSystem:
    def __init__(self, steps):
        self.steps = steps
        self.current_step = 0

    def get_current_step(self):
        if self.current_step < len(self.steps):
            return self.steps[self.current_step]
        else:
            return None

    def mark_step_as_completed(self):
        if self.current_step < len(self.steps):
            if self.steps[self.current_step].status == RepairStepStatus.COMPLETED:
                raise ValueError("Step is already completed")
            self.steps[self.current_step].status = RepairStepStatus.COMPLETED
            self.current_step += 1
        else:
            raise ValueError("All steps are completed")

    def get_progress(self):
        completed_steps = sum(1 for step in self.steps if step.status == RepairStepStatus.COMPLETED)
        return completed_steps / len(self.steps)

    def provide_feedback(self):
        if self.get_progress() == 1:
            return "Repair completed successfully"
        else:
            return "Please complete the remaining steps"
