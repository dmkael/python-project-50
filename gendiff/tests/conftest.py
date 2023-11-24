from pathlib import Path
import pytest


@pytest.fixture
def get_fixtures_dir():
    current_dir = Path(__file__).parent
    fixtures_dir = current_dir / "fixtures"
    return fixtures_dir
