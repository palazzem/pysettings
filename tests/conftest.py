import pytest

from .fixtures.settings import TestValidSettings


@pytest.fixture(scope="function")
def test_settings():
    settings = TestValidSettings()
    settings.is_valid()
    yield settings
