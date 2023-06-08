import copy
import pytest

from .fixtures import settings as config


@pytest.fixture
def settings():
    previous_config = copy.deepcopy(config.settings)
    yield config.settings
    config.settings = previous_config
