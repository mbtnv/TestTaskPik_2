import pytest
from metro_verificate.main import init_app


@pytest.fixture
async def client(test_client):
    app = await init_app()
    return await test_client(app)
