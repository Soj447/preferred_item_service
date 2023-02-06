from dataclasses import dataclass
from typing import List, Tuple

from preferred_item_service.domain.value_objects import (
    Brick,
    ItemStatus,
    Price,
)


@dataclass
class Item:
    id: int
    bricks: List[Brick]

    def contains(self, target_bricks: List[Brick]) -> bool:
        for brick in target_bricks:
            if brick not in self.bricks:
                return False
        return True


@dataclass
class MasterData:
    item_id: int
    status: ItemStatus
    price: Price


FullItemInformation = Tuple[Item, MasterData]
PreferredItem = Item
