import json
import logging
from app.llm.client import LLMClient
from app.config.gcn_nasa_settings import GCNNasaSettings
from app.pipeline.state import AlertState

logger = logging.getLogger(__name__)


def make_enrich_node(llm_client: LLMClient, settings: GCNNasaSettings):

    def enrich_node(state: AlertState) -> dict:
        try:
            classification = state["classification"]
            raw_alert = state["raw_alert"]
            content = f"""
                            Aqui estão os dados para análise:

                            ### CLASSIFICAÇÃO:
                            {classification}

                            ### ALERT BRUTO (RAW ALERT):
                            {json.dumps(raw_alert, indent=2)}

                            Gere a análise baseada em ambos os contextos acima.
                        """

            result = llm_client.chat(
                settings.LLM_MODEL_FAST,
                [
                    {
                        "role": "system",
                        "content": """
                                - Explicar a relevância científica do evento  
                            """,
                    },
                    {"role": "user", "content": content},
                ],
            )

            # Retorna APENAS as chaves que quer atualizar
            return {"analysis": result}
        
        except Exception as ex:
            logger.error("Falha ao executar enrich_node: ", ex)

    return enrich_node
