import pytest
from aiohttp import web
from pytest_aiohttp.plugin import AiohttpClient


@pytest.mark.asyncio
async def test_happy_path(
    web_app: web.Application, aiohttp_client: AiohttpClient
) -> None:
    client = await aiohttp_client(web_app)
    post_data = {"bricks": [{"design_id": 2, "color_codes": [255, 255]}]}
    expected_response = {
        "item": {
            "id": 14,
            "bricks": [
                {"design_id": 0, "color_codes": [255, 255]},
                {"design_id": 2, "color_codes": [255, 255]},
            ],
        }
    }
    resp = await client.post("/", json=post_data)
    assert resp.status == 200
    result = await resp.json()
    assert result == expected_response


@pytest.mark.asyncio
async def test_error_on_wrong_http_method(
    web_app: web.Application, aiohttp_client: AiohttpClient
) -> None:
    client = await aiohttp_client(web_app)
    resp = await client.get("/")
    assert resp.status == 405

    resp = await client.put("/", data={})
    assert resp.status == 405

    resp = await client.patch("/", data={})
    assert resp.status == 405


@pytest.mark.asyncio
async def test_not_found_error_on_missing_bricks(
    web_app: web.Application, aiohttp_client: AiohttpClient
) -> None:
    client = await aiohttp_client(web_app)
    post_data = {"bricks": [{"design_id": 447, "color_codes": [0, 225]}]}
    resp = await client.post("/", json=post_data)
    assert resp.status == 404


@pytest.mark.asyncio
async def test_server_error_on_services_unsync(
    web_app_with_unsync_services: web.Application,
    aiohttp_client: AiohttpClient,
) -> None:
    client = await aiohttp_client(web_app_with_unsync_services)
    post_data = {"bricks": [{"design_id": 3, "color_codes": [255, 255]}]}
    resp = await client.post("/", json=post_data)
    assert resp.status == 500


@pytest.mark.asyncio
async def test_bad_request_on_invalid_data(
    web_app: web.Application, aiohttp_client: AiohttpClient
) -> None:
    client = await aiohttp_client(web_app)
    invalid_value_type_of_design_id = {
        "bricks": [{"design_id": "wrong_type", "color_codes": [255, 255]}]
    }
    resp = await client.post("/", json=invalid_value_type_of_design_id)
    assert resp.status == 400

    invalid_value_type_of_color_codes = {
        "bricks": [{"design_id": 0, "color_codes": ["asd", "fdf"]}]
    }
    resp = await client.post("/", json=invalid_value_type_of_color_codes)
    assert resp.status == 400

    missing_design_id = {"bricks": [{"color_codes": [255, 255]}]}
    resp = await client.post("/", json=missing_design_id)
    assert resp.status == 400

    missing_color_codes = {"bricks": [{"design_id": 0}]}
    resp = await client.post("/", json=missing_color_codes)
    assert resp.status == 400
