import json
import logging
from app.llm.llm_client import LLMClient
from app.config.llm_models import LLMModels
from app.pipeline.state import AlertState
from app.pipeline.utils import extract_json

logger = logging.getLogger(__name__)


def make_classify_node(llm_client: LLMClient):
    """Fábrica do nó de classificação.

    Usa ``LLMModels.CLASSIFIER`` como modelo — constante definida em
    ``config/llm_models.py``, sem necessidade de injeção de dependência.
    """

    def classify_node(state: AlertState) -> dict:
        try:
            raw_alert = state["raw_alert"]

            result = llm_client.chat(
                LLMModels.CLASSIFIER,
                [
                    {
                        "role": "system",
                        "content": """
                                - Identifique tipo do evento, missão de origem, coordenadas (se houver), nível de urgência.
                                - Retorne em formato estruturado JSON com campos fixos.
                                - Exemplo de retorno "{"classification": "...", "alert_type": "GRB"}"   
                            """,
                    },
                    {"role": "user", "content": json.dumps(raw_alert, indent=2)},
                ],
            )

            parsed = extract_json(result)
            # Fallback: retorna tipo genérico se não conseguir parsear
            if not parsed:
                return {"classification": result, "alert_type": "UNKNOWN"}
            return parsed

        except Exception as ex:
            logger.error("Falha ao executar classify_node: %s", ex)
            raise

    return classify_node
