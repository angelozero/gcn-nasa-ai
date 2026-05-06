class LLMModels:
    """Constantes com os aliases dos modelos LLM registrados no proxy LiteLLM.

    Uso direto — sem instanciação, sem injeção de dependência:

        from app.config.llm_models import LLMModels

        llm_client.chat(LLMModels.CLASSIFIER, messages)
    """

    CLASSIFIER: str = "nasa-classifier"
    EMBEDDER: str = "nasa-embedder"
    FAST: str = "nasa-fast"
    OLLAMA_EMBEDDER: str = "ollama-embedder"
