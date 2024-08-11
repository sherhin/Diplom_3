import pytest

from data import Urls
from .api_client import ApiClient

@pytest.fixture
def api_client():
    api_client = ApiClient(base_url=Urls.MAIN_PAGE)
    return api_client

