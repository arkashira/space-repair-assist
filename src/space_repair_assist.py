import json
from dataclasses import dataclass
from typing import List

@dataclass
class FaultLog:
    log_data: str

@dataclass
class ProbableCause:
    cause: str
    confidence_score: float
    repair_procedure: str

class DiagnosticEngine:
    def __init__(self):
        self.fault_logs = []

    def upload_fault_log(self, log_data: str) -> None:
        if len(log_data) <= 10 * 1024 * 1024:  # 10 MB
            self.fault_logs.append(FaultLog(log_data))
        else:
            raise ValueError("Log data exceeds 10 MB limit")

    def diagnose(self) -> List[ProbableCause]:
        # Simulate diagnosis logic
        causes = [
            ProbableCause("Cause 1", 0.8, "Repair Procedure 1"),
            ProbableCause("Cause 2", 0.5, "Repair Procedure 2"),
            ProbableCause("Cause 3", 0.2, "Repair Procedure 3"),
        ]
        return causes

    def get_top_causes(self, num_causes: int) -> List[ProbableCause]:
        causes = self.diagnose()
        return sorted(causes, key=lambda x: x.confidence_score, reverse=True)[:num_causes]
