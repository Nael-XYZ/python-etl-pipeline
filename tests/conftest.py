"""Pytest fixtures."""
import pytest, tempfile

@pytest.fixture
def temp_dir():
    with tempfile.TemporaryDirectory() as d: yield d

@pytest.fixture
def sample_config():
    return {"model": "default", "version": "1.0.0", "debug": False}
