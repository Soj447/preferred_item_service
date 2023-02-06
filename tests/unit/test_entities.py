from preferred_item_service.domain.entities import Item
from preferred_item_service.domain.value_objects import Brick


def test_item_can_identify_if_it_contains_list_of_bricks() -> None:
    target_bricks = [
        Brick(0, [11, 12]),
        Brick(2, [255, 0]),
        Brick(2, [255, 255]),
    ]
    item = Item(0, target_bricks)
    assert item.contains(target_bricks)
    assert item.contains(target_bricks[1:])

    item2 = Item(1, target_bricks[2:])
    assert not item2.contains(target_bricks)
    assert item2.contains(target_bricks[2:])
    assert not item2.contains([Brick(4, [11, 12])])


def test_ensure_that_color_code_order_matters() -> None:
    first_brick = Brick(0, [12, 11])
    identical_brick = Brick(0, [12, 11])
    second_brick = Brick(0, [11, 12])

    assert first_brick != second_brick
    assert first_brick == identical_brick
