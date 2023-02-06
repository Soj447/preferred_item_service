from dataclasses import asdict

from aiohttp import web
from pydantic import BaseModel, ValidationError, conlist

from preferred_item_service.domain.errors import (
    NoItemsFoundWithSpecifiedBricks,
    NotEnoughMasterData,
)
from preferred_item_service.domain.service import PreferredItemService
from preferred_item_service.domain.value_objects import Brick


class GetPreferredItemSchema(BaseModel):
    bricks: conlist(Brick, min_items=1)  # type: ignore


class RestInterface:
    def __init__(self, service: PreferredItemService):
        self._service = service
        self.app = web.Application()
        self._setup_router()

    def run(self, host: str, port: int) -> None:
        web.run_app(self.app, host=host, port=port)

    def _setup_router(self) -> None:
        self.app.router.add_post("/", self.get_preferred_item)

    async def get_preferred_item(self, request: web.Request) -> web.Response:
        data = await request.json()
        try:
            requested_bricks = GetPreferredItemSchema.parse_obj(data).bricks
            preferred_item = await self._service.find(requested_bricks)
        except NoItemsFoundWithSpecifiedBricks:
            raise web.HTTPNotFound()
        except NotEnoughMasterData:
            raise web.HTTPInternalServerError(
                text="Master Data Service and Item Service mismatch"
            )
        except ValidationError as e:
            raise web.HTTPBadRequest(text=str(e))
        return web.json_response({"item": asdict(preferred_item)})
