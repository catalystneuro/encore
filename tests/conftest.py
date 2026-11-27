"""The registry's tests run with the protocol laid over the checkout (tools/protocol.sh)."""
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def pytest_configure(config):
    if not (ROOT / "tools" / "agent_run.py").is_file():
        pytest.exit("The protocol is not laid over this checkout: run tools/protocol.sh first.", returncode=4)
