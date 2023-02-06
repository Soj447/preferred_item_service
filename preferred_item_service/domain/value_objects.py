from dataclasses import dataclass
from enum import Enum, auto
from typing import List, TypeAlias

ColorCode: TypeAlias = int
Price: TypeAlias = int


@dataclass
class Brick:
    design_id: int
    color_codes: List[ColorCode]


class ItemStatus(int, Enum):
    Discountinued = auto()
    Outgoing = auto()
    Novelty = auto()
    Normal = auto()
