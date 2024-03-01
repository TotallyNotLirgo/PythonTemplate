from functools import lru_cache
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    WELCOME_MESSAGE: str
    HOST: str
    PORT: int

    DEV_MODE: bool
    LOG_LEVEL: str
    LOG_FILE: str
    CONSOLE_ENABLED: bool

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_config() -> Config:
    return Config()
