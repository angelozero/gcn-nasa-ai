import re
import json
import logging
from app.llm.client import LLMClient
from app.config.gcn_nasa_settings import GCNNasaSettings
from app.pipeline.state import AlertState

logger = logging.getLogger(__name__)

def make_classify_node(llm_client: LLMClient, settings: GCNNasaSettings):

    def classify_node(state: AlertState) -> dict:

        try:
            raw_alert = state["raw_alert"]

            result = llm_client.chat(
                settings.LLM_MODEL_CLASSIFIER,
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

            return _parse_classification(result)
        
        except Exception as ex:
            logger.error("Falha ao executar classify_node: ", ex)

    return classify_node
 

def _parse_classification(llm_response: str) -> dict:
        """Extrai o JSON da resposta da LLM, mesmo com texto ao redor."""
        # Tenta encontrar um bloco JSON na resposta
        match = re.search(r"\{.*\}", llm_response, re.DOTALL)
        if match:
            try:
                return json.loads(match.group())
            except json.JSONDecodeError:
                pass
        # Fallback: retorna tipo genérico se não conseguir parsear
        return {"classification": llm_response, "alert_type": "UNKNOWN"}