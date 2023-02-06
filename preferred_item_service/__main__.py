import logging

from preferred_item_service.bootstrap import bootstrap_app
from preferred_item_service.config import app_settings


def startup() -> None:
    logging.basicConfig(level=logging.DEBUG)
    app = bootstrap_app()
    app.run(app_settings.HOST, app_settings.PORT)


if __name__ == "__main__":
    startup()
