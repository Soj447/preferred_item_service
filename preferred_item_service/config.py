from pathlib import Path

from pydantic import BaseSettings


class AppSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8080
    PROJ_DIR: Path = Path(__file__).parent


app_settings = AppSettings()
