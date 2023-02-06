from typing import Tuple
from unittest.mock import AsyncMock

import pytest
from aiohttp import web

from preferred_item_service.adapters.aiohttp import RestInterface
from preferred_item_service.adapters.item_service import DummyItemService
from preferred_item_service.adapters.master_data_service import (
    DummyMasterDataService,
)
from preferred_item_service.bootstrap import bootstrap_app
from preferred_item_service.domain.entities import Brick, Item, MasterData
from preferred_item_service.domain.ports import ItemService, MasterDataService
from preferred_item_service.domain.service import PreferredItemService
from preferred_item_service.domain.value_objects import ItemStatus


@pytest.fixture()
def web_app() -> web.Application:
    return bootstrap_app().app


@pytest.fixture()
def web_app_with_unsync_services(
    unsynced_services: Tuple[MasterDataService, ItemService]
) -> web.Application:
    service = PreferredItemService(*unsynced_services)
    app = RestInterface(service).app
    return app


@pytest.fixture()
def empty_master_data_service() -> MasterDataService:
    master_data_service = DummyMasterDataService()
    master_data_service.get_all = AsyncMock(return_value=[])
    return master_data_service


@pytest.fixture()
def empty_item_service() -> ItemService:
    item_service = DummyItemService()
    item_service.get_all = AsyncMock(return_value=[])
    return item_service


@pytest.fixture()
def synced_services() -> Tuple[MasterDataService, ItemService]:
    master_data_list = [
        MasterData(*x)
        for x in [
            [0, ItemStatus.Normal, 100],
            [1, ItemStatus.Discountinued, 100],
            [2, ItemStatus.Novelty, 100],
            [3, ItemStatus.Outgoing, 100],
            [4, ItemStatus.Normal, 200],
            [5, ItemStatus.Novelty, 5],
            [6, ItemStatus.Outgoing, 10],
        ]
    ]

    items = [
        Item(*x)
        for x in [
            [0, [Brick(0, [255, 255])]],
            [1, [Brick(1, [255, 255])]],
            [2, [Brick(2, [255, 255])]],
            [3, [Brick(3, [255, 255])]],
            [4, [Brick(0, [255, 255]), Brick(2, [255, 255])]],
            [5, [Brick(0, [255, 255])]],
            [6, [Brick(0, [255, 255])]],
        ]
    ]

    master_data_service = DummyMasterDataService()
    item_service = DummyItemService()
    master_data_service.get_all = AsyncMock(return_value=master_data_list)
    item_service.get_all = AsyncMock(return_value=items)

    return master_data_service, item_service


@pytest.fixture()
def unsynced_services() -> Tuple[MasterDataService, ItemService]:
    master_data_list = [
        MasterData(*x)
        for x in [
            [0, ItemStatus.Normal, 100],
            [1, ItemStatus.Discountinued, 100],
            [2, ItemStatus.Novelty, 100],
        ]
    ]

    items = [
        Item(*x)
        for x in [
            [0, [Brick(0, [255, 255])]],
            [1, [Brick(1, [255, 255])]],
            [2, [Brick(2, [255, 255])]],
            [3, [Brick(3, [255, 255])]],
            [4, [Brick(0, [255, 255]), Brick(2, [255, 255])]],
            [5, [Brick(0, [255, 255])]],
            [6, [Brick(0, [255, 255])]],
        ]
    ]

    master_data_service = DummyMasterDataService()
    item_service = DummyItemService()
    master_data_service.get_all = AsyncMock(return_value=master_data_list)
    item_service.get_all = AsyncMock(return_value=items)

    return master_data_service, item_service
