import pytest


SYSTEM_VERSION = "v1.2.0"


@pytest.mark.skipif(
    condition=SYSTEM_VERSION == "v1.3.0",
    reason="Test not available in system 1.3.0"
)
def test_system_version_valid():
    ...
@pytest.mark.skipif(
    condition=SYSTEM_VERSION == "v1.2.0",
reason="Test not available in system 1.3.0"
)
def test_system_version_invalid():
    ...