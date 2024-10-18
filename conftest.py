import pytest
from playwright.sync_api import sync_playwright
from api.petstore_api import PetstoreAPI
from utils import config

@pytest.fixture(scope="session")
def api_request_context():
    with sync_playwright() as p:
        request_context = p.request.new_context(base_url=config.BASE_URL)
        yield request_context
        request_context.dispose()

@pytest.fixture(scope="session")
def petstore_api(api_request_context):
    return PetstoreAPI(api_request_context)
