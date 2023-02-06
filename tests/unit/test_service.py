from typing import Tuple

import pytest

from preferred_item_service.domain.entities import Brick
from preferred_item_service.domain.errors import (
    NoItemsFoundWithSpecifiedBricks,
    NotEnoughMasterData,
)
from preferred_item_service.domain.ports import ItemService, MasterDataService
from preferred_item_service.domain.service import PreferredItemService


@pytest.mark.asyncio
async def test_raises_exception_if_other_services_return_nothing(
    empty_master_data_service: MasterDataService,
    empty_item_service: ItemService,
) -> None:
    with pytest.raises(NoItemsFoundWithSpecifiedBricks):
        service = PreferredItemService(
            empty_master_data_service, empty_item_service
        )
        await service.find([Brick(0, [255, 255])])


@pytest.mark.asyncio
async def test_raises_exception_if_no_brick_with_requested_color_exists(
    synced_services: Tuple[MasterDataService, ItemService]
) -> None:
    with pytest.raises(NoItemsFoundWithSpecifiedBricks):
        master_data_service, item_service = synced_services
        service = PreferredItemService(master_data_service, item_service)
        await service.find([Brick(0, [11, 123])])


@pytest.mark.asyncio
async def test_raises_exception_if_no_brick_with_requested_design_exists(
    synced_services: Tuple[MasterDataService, ItemService]
) -> None:
    with pytest.raises(NoItemsFoundWithSpecifiedBricks):
        master_data_service, item_service = synced_services
        service = PreferredItemService(master_data_service, item_service)
        await service.find([Brick(9999, [255, 255])])


@pytest.mark.asyncio
async def test_raises_exception_if_master_data_misses_information_about_item(
    unsynced_services: Tuple[MasterDataService, ItemService]
) -> None:
    with pytest.raises(NotEnoughMasterData):
        service = PreferredItemService(*unsynced_services)
        await service.find([Brick(0, [255, 255]), Brick(2, [255, 255])])


@pytest.mark.asyncio
async def test_can_find_preferred_item(
    synced_services: Tuple[MasterDataService, ItemService]
) -> None:
    master_data_service, item_service = synced_services
    target_item = (await item_service.get_all())[4]

    service = PreferredItemService(master_data_service, item_service)
    found_item = await service.find(
        [Brick(0, [255, 255]), Brick(2, [255, 255])]
    )
    assert found_item.id == target_item.id


@pytest.mark.asyncio
async def test_prefers_status_to_lower_price(
    synced_services: Tuple[MasterDataService, ItemService]
) -> None:
    master_data_service, item_service = synced_services
    target_item = (await item_service.get_all())[0]

    service = PreferredItemService(master_data_service, item_service)
    found_item = await service.find(target_item.bricks)
    assert found_item.id == target_item.id
