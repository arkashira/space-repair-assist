import pytest
from space_repair_assist import DiagnosticEngine, FaultLog, ProbableCause

def test_upload_fault_log():
    engine = DiagnosticEngine()
    log_data = "Sample log data"
    engine.upload_fault_log(log_data)
    assert len(engine.fault_logs) == 1

def test_upload_fault_log_exceeds_limit():
    engine = DiagnosticEngine()
    log_data = "a" * (10 * 1024 * 1024 + 1)  # 10 MB + 1 byte
    with pytest.raises(ValueError):
        engine.upload_fault_log(log_data)

def test_diagnose():
    engine = DiagnosticEngine()
    causes = engine.diagnose()
    assert len(causes) == 3

def test_get_top_causes():
    engine = DiagnosticEngine()
    top_causes = engine.get_top_causes(2)
    assert len(top_causes) == 2
    assert top_causes[0].confidence_score == 0.8
    assert top_causes[1].confidence_score == 0.5
