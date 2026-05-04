import json
from app.llm.client import LLMClient
from app.config.gcn_nasa_settings import GCNNasaSettings
from app.pipeline.state import AlertState


def make_summarize_node(llm_client: LLMClient, settings: GCNNasaSettings):

    def summarize_node(state: AlertState) -> dict:
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
            settings.LLM_MODEL_CLASSIFIER,
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

    return summarize_node
