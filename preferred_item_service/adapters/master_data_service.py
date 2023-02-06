from typing import List

from preferred_item_service.domain.entities import MasterData
from preferred_item_service.domain.ports import MasterDataService
from preferred_item_service.domain.value_objects import ItemStatus


class DummyMasterDataService(MasterDataService):
    async def get_all(self) -> List[MasterData]:
        return [
            MasterData(*data)
            for data in [
                (0, ItemStatus.Discountinued, 10),
                (1, ItemStatus.Discountinued, 5),
                (2, ItemStatus.Novelty, 50),
                (3, ItemStatus.Outgoing, 30),
                (4, ItemStatus.Normal, 500),
                (5, ItemStatus.Normal, 250),
                (6, ItemStatus.Normal, 350),
                (7, ItemStatus.Outgoing, 100),
                (8, ItemStatus.Discountinued, 10),
                (9, ItemStatus.Normal, 50),
                (10, ItemStatus.Discountinued, 10),
                (11, ItemStatus.Novelty, 50),
                (12, ItemStatus.Outgoing, 50),
                (13, ItemStatus.Novelty, 50),
                (14, ItemStatus.Normal, 200),
            ]
        ]
