import json
import logging
from app.llm.llm_client import LLMClient
from app.config.llm_models import LLMModels
from app.pipeline.state import AlertState

logger = logging.getLogger(__name__)


def make_enrich_node(llm_client: LLMClient):
    """Fábrica do nó de enriquecimento.

    Usa ``LLMModels.FAST`` como modelo — constante definida em
    ``config/llm_models.py``, sem necessidade de injeção de dependência.
    """

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
                LLMModels.FAST,
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
            logger.error("Falha ao executar enrich_node: %s", ex)
            raise

    return enrich_node
