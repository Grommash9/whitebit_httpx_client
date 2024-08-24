from conftest import vcr_c  # noqa
import pytest
from whitebit_httpx_client import WhiteBITClient  # noqa


@pytest.mark.xfail(reason="waiting for api keys")
@vcr_c.use_cassette("assets/create_deposit_address.yaml")
def test_get_assets(white_bit_client: WhiteBITClient):
    _ = white_bit_client.create_deposit_address("USDT", "ERC20")


@pytest.mark.xfail(reason="waiting for api keys")
@vcr_c.use_cassette("assets/create_deposit_address.yaml")
async def test_async_get_assets(white_bit_client: WhiteBITClient):
    _ = await white_bit_client.async_create_deposit_address("USDT", "ERC20")
