import pytest

@pytest.fixture(scope="function", name="login")
def login():
    sn = "123"
    yield sn