from typing import TypedDict

class AlertState(TypedDict):
    # Input
    raw_alert: dict           # O JSON bruto do GCN
    topic: str                # O tópico Kafka de origem

    # Processamento
    alert_type: str           # "GRB", "GW", "FRB", "Neutrino", etc.
    classification: str       # Resultado do nó de classificação
    rag_context: list[str]    # Documentos recuperados pelo RAG
    
    # Output
    analysis: str             # Análise enriquecida
    summary: str              # Sumário final estruturado
    
    # Controle
    error: str | None         # Se algo deu errado
    retry_count: int          # Para evitar loops infinitos