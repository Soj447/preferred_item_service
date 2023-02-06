from preferred_item_service.adapters.aiohttp import RestInterface
from preferred_item_service.adapters.item_service import DummyItemService
from preferred_item_service.adapters.master_data_service import (
    DummyMasterDataService,
)
from preferred_item_service.domain.service import PreferredItemService


def bootstrap_app() -> RestInterface:
    master_data_service = DummyMasterDataService()
    item_service = DummyItemService()
    service = PreferredItemService(master_data_service, item_service)

    app = RestInterface(service)
    return app
