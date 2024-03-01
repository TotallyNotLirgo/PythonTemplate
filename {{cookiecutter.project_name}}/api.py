from general.config import get_config
from general.logger import init_logger
from logging import getLogger
from dataclasses import dataclass
from fastapi import FastAPI

config = get_config()
init_logger(config.LOG_LEVEL, config.LOG_FILE, config.CONSOLE_ENABLED)
logger = getLogger(__name__)


@dataclass
class BasicResponse:
    message: str = "OK"


app = FastAPI()


@app.get("/")
def get_root() -> BasicResponse:
    return BasicResponse(config.WELCOME_MESSAGE)
