import json
import logging
import time

from gcn_kafka import Consumer
from app.config.gcn_nasa_settings import GCNNasaSettings
from app.llm.client import LLMClient
from app.models import TOPIC_MODEL_MAP
from app.pipeline.graph import create_pipeline

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)


def main() -> None:
    settings = GCNNasaSettings()
    
    llm_client = LLMClient()

    pipeline = create_pipeline(llm_client=llm_client)

    consumer = Consumer(
        client_id=settings.GCN_NASA_CLIENT_ID,
        client_secret=settings.GCN_NASA_CLIENT_SECRET.get_secret_value(),
    )
    consumer.subscribe(settings.GCN_NASA_ALERTS)

    duracao = settings.CONSUMER_DURATION
    logger.info("Consumidor GCN iniciado. Executando por %d segundo(s)...", duracao)

    dict_test = {}
    keep = True

    inicio = time.monotonic()
    try:
        # while (time.monotonic() - inicio) < duracao:
        while keep:
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

                    # if topic != "gcn.heartbeat":
                    # result = pipeline.invoke(
                    #     {
                    #         "raw_alert": value,  # dict original, completo
                    #         "topic": topic,
                    #     }
                    # )

                    # logger.info(
                    #     "[FINAL] Sumário gerado: %s", result.get("summary", "N/A")
                    # )

                    dict_test = model_class
                    keep = False

                except Exception:
                    logger.exception(
                        "Erro de validação na mensagem do tópico %s", topic
                    )
    finally:
        consumer.close()
        logger.info(
            "Consumidor encerrado após %.1f segundo(s).",
            time.monotonic() - inicio,
        )
    print("\nLANGGRAPH")
    result = pipeline.invoke(
        {
            "raw_alert": value,  # dict original, completo
            "topic": dict_test,
        }
    )
    
    print(result)


if __name__ == "__main__":
    main()
