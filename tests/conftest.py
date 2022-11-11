import pytest
from connect.client import AsyncConnectClient, ConnectClient


@pytest.fixture
def connect_client():
    return ConnectClient(
        'ApiKey fake_api_key',
        endpoint='https://example.org/public/v1',
    )


@pytest.fixture
def async_connect_client():
    return AsyncConnectClient(
        'ApiKey fake_api_key',
        endpoint='https://example.org/public/v1',
    )


@pytest.fixture
def logger(mocker):
    return mocker.MagicMock()
