from typing import List

from preferred_item_service.domain.entities import Item
from preferred_item_service.domain.ports import ItemService
from preferred_item_service.domain.value_objects import Brick


class DummyItemService(ItemService):
    async def get_all(self) -> List[Item]:
        return [
            Item(*item_data)
            for item_data in [
                (0, [Brick(0, [255, 255])]),
                (1, [Brick(1, [255, 1])]),
                (2, [Brick(0, [1, 255])]),
                (3, [Brick(2, [255, 255])]),
                (
                    4,
                    [
                        Brick(0, [255, 255]),
                        Brick(1, [255, 1]),
                        Brick(2, [255, 255]),
                    ],
                ),
                (5, [Brick(1, [255, 255]), Brick(0, [80, 80])]),
                (
                    6,
                    [
                        Brick(0, [80, 80]),
                        Brick(0, [255, 255]),
                        Brick(2, [255, 255]),
                    ],
                ),
                (7, [Brick(2, [80, 80])]),
                (8, [Brick(1, [1, 255])]),
                (9, [Brick(0, [255, 1])]),
                (10, [Brick(0, [255, 1]), Brick(2, [255, 255])]),
                (11, [Brick(2, [5, 10])]),
                (12, [Brick(2, [10, 5])]),
                (13, [Brick(2, [10, 5])]),
                (14, [Brick(0, [255, 255]), Brick(2, [255, 255])]),
            ]
        ]
