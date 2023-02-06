from typing import List

from preferred_item_service.domain.entities import (
    FullItemInformation,
    Item,
    MasterData,
)


def map_items_to_master_data(
    items: List[Item], master_data_list: List[MasterData]
) -> List[FullItemInformation]:
    items_full_info = []

    for item in items:
        for master_data in master_data_list:
            if item.id != master_data.item_id:
                continue
            items_full_info.append((item, master_data))
    return items_full_info
