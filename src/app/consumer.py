import json
import logging
import time

from gcn_kafka import Consumer

from app.config.gcn_nasa_settings import GCNNasaSettings
from app.models import TOPIC_MODEL_MAP

MAX_SCANS = 5

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)


def main() -> None:
    settings = GCNNasaSettings()

    consumer = Consumer(
        client_id=settings.GCN_NASA_CLIENT_ID,
        client_secret=settings.GCN_NASA_CLIENT_SECRET.get_secret_value(),
    )
    consumer.subscribe(settings.GCN_NASA_ALERTS)

    logger.info("Consumidor GCN iniciado. Executando %d varreduras...", MAX_SCANS)

    try:
        for scan in range(1, MAX_SCANS + 1):
            logger.info("Varredura %d/%d", scan, MAX_SCANS)

            for message in consumer.consume(timeout=1):
                if message.error():
                    logger.error("Erro no Kafka: %s", message.error())
                    continue

                topic = message.topic()
                raw = message.value()

                try:
                    value = json.loads(raw)
                except (json.JSONDecodeError, TypeError):
                    logger.exception("Falha ao decodificar JSON do tópico %s", topic)
                    continue

                model_class = TOPIC_MODEL_MAP.get(topic)
                if model_class is None:
                    logger.warning("Tópico desconhecido: %s", topic)
                    continue

                try:
                    parsed = model_class(**value)
                    logger.info(
                        "[%s] Mensagem parseada: %s",
                        topic,
                        parsed.model_dump_json()[:200],
                    )
                except Exception:
                    logger.exception("Erro de validação na mensagem do tópico %s", topic)

            if scan < MAX_SCANS:
                time.sleep(2)
    finally:
        consumer.close()
        logger.info("Consumidor encerrado com sucesso.")

    logger.info("Todas as %d varreduras concluídas.", MAX_SCANS)


if __name__ == "__main__":
    main()