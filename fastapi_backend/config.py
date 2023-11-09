from pathlib import Path

from pydantic import BaseSettings

HERE = Path(__file__).resolve().parent


class Settings(BaseSettings):
    pass

settings = Settings()
