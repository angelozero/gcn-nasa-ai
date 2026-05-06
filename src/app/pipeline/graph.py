import logging
from langgraph.graph import StateGraph, END
from app.pipeline.state import AlertState
from app.pipeline.nodes.classify import make_classify_node
from app.pipeline.nodes.enrich import make_enrich_node
from app.pipeline.nodes.summarize import make_summarize_node
from app.pipeline.nodes.persist import persist_node
from app.config.gcn_nasa_settings import KNOWN_TYPES

logger = logging.getLogger(__name__)


def route_after_classify(state: AlertState) -> str:
    alert_type = state.get("alert_type", "UNKNOWN").upper()
    if alert_type not in KNOWN_TYPES:
        logger.warning("Alerta ignorado — tipo: %s", alert_type)
        return END
    return "enrich"


def create_pipeline(llm_client):
    """Monta e compila o pipeline LangGraph.

    Os modelos LLM são constantes definidas em LLMModels — cada nó
    os importa diretamente, sem necessidade de injeção via parâmetro.

    Args:
        llm_client: cliente LLM para chamadas ao proxy LiteLLM.
    """
    graph = StateGraph(AlertState)
    graph.add_node("classify", make_classify_node(llm_client))
    graph.add_node("enrich", make_enrich_node(llm_client))
    graph.add_node("summarize", make_summarize_node(llm_client))
    graph.add_node("persist", persist_node)

    graph.set_entry_point("classify")

    graph.add_conditional_edges("classify", route_after_classify)

    graph.add_edge("enrich", "summarize")
    graph.add_edge("summarize", "persist")
    graph.add_edge("persist", END)

    return graph.compile()
