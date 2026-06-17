import logging

logging.basicConfig(
    level=logging.info,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("my_log.log" , encoding="utf-8")
    ]
)

logger = logging.getLogger(__name__)
