import re
import pytest

WORK_ID_PATTERN = re.compile(r"[A-Z]+-\d+")

def test_valid_work_id_in_branch():
    assert WORK_ID_PATTERN.search("feat/FIN-123-my-feature")

def test_missing_work_id_in_branch():
    assert not WORK_ID_PATTERN.search("feat/my-feature-without-id")

def test_valid_work_id_formats():
    valid = ["FIN-123", "PROJ-9999", "ABC-1"]
    for wid in valid:
        assert WORK_ID_PATTERN.search(wid), f"Debería ser válido: {wid}"