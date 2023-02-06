from abc import ABC, abstractmethod
from typing import List

from preferred_item_service.domain.entities import Item, MasterData


class MasterDataService(ABC):
    @abstractmethod
    async def get_all(self) -> List[MasterData]:
        raise NotImplementedError()


class ItemService(ABC):
    @abstractmethod
    async def get_all(self) -> List[Item]:
        raise NotImplementedError()
