from app.pipeline.state import AlertState
import logging

logger = logging.getLogger(__name__)

def persist_node(state: AlertState) -> dict:
    logger.info("PERSIST (stub): %s", state.get("summary"))
    return {}