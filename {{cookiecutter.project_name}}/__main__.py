import uvicorn
from general.config import get_config
import logging

config = get_config()

if __name__ == "__main__":
    uvicorn.run(
        "api:app",
        host=config.HOST,
        port=config.PORT,
        reload=config.DEV_MODE,
        log_level=logging.getLevelName(config.LOG_LEVEL)
    )
