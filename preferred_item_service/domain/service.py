import asyncio
from typing import List

from preferred_item_service.domain.entities import (
    Brick,
    FullItemInformation,
    PreferredItem,
)
from preferred_item_service.domain.errors import (
    NoItemsFoundWithSpecifiedBricks,
    NotEnoughMasterData,
)
from preferred_item_service.domain.helpers import map_items_to_master_data
from preferred_item_service.domain.ports import ItemService, MasterDataService


class PreferredItemService:
    def __init__(
        self, master_data_service: MasterDataService, item_service: ItemService
    ):
        self.__master_data_service = master_data_service
        self.__item_service = item_service

    async def find(self, bricks: List[Brick]) -> PreferredItem:
        all_items, all_master_data = await asyncio.gather(
            self.__item_service.get_all(),
            self.__master_data_service.get_all(),
        )
        found_items = [item for item in all_items if item.contains(bricks)]
        if not found_items:
            raise NoItemsFoundWithSpecifiedBricks()

        full_items_information = map_items_to_master_data(
            found_items, all_master_data
        )
        preferred_item, _ = self._choose_preferred_item_information(
            full_items_information
        )
        return preferred_item

    @staticmethod
    def _choose_preferred_item_information(
        full_items_information: List[FullItemInformation],
    ) -> FullItemInformation:
        if not full_items_information:
            raise NotEnoughMasterData()

        preferred_item_information = full_items_information[0]

        for full_item_information in full_items_information:
            _, master_data = full_item_information
            _, preferred_master_data = preferred_item_information

            if master_data.status < preferred_master_data.status:
                continue
            elif (
                master_data.status > preferred_master_data.status
                or master_data.price < preferred_master_data.price
            ):
                preferred_item_information = full_item_information
        return preferred_item_information
