import json
import logging
from app.llm.client import LLMClient
from app.config.llm_models import LLMModels
from app.pipeline.state import AlertState

logger = logging.getLogger(__name__)

def make_summarize_node(llm_client: LLMClient):
    """Fábrica do nó de sumarização.

    Usa ``LLMModels.CLASSIFIER`` como modelo — constante definida em
    ``config/llm_models.py``, sem necessidade de injeção de dependência.
    """

    def summarize_node(state: AlertState) -> dict:
        try:
            raw_alert = state["raw_alert"]
            analysis = state["analysis"]

            content = f"""
                        - Gere o sumário estruturado em JSON com os campos solicitados.
                        
                        ### ANÁLISE (ANALYSIS):
                        {analysis}

                        ### ALERT BRUTO (RAW ALERT):
                        {json.dumps(raw_alert, indent=2)}
                """

            result = llm_client.chat(
                LLMModels.CLASSIFIER,
                [
                    {
                        "role": "system",
                        "content": """
                                - Gere o sumário estruturado em JSON com base na análise e no alerta bruto
                                        - event_id: identificador do evento
                                        - event_type: tipo classificado
                                        - significance: relevância científica (1-5)
                                        - summary_text: texto em linguagem natural
                                        - recommended_action: o que um astrônomo deveria fazer com essa informação  
                            """,
                    },
                    {"role": "user", "content": content},
                ],
            )

            # Retorna APENAS as chaves que quer atualizar
            return {"summary": result}
        except Exception as ex:
            logger.error("Falha ao executar summarize_node: ", ex.message)
            raise RuntimeError("Falha ao executar summarize_node: %s" % (ex.message))
            
    return summarize_node
