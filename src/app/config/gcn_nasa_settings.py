from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class GCNNasaSettings(BaseSettings):
    """Configurações centralizadas do GCN NASA carregadas do arquivo .env."""

    # ── GCN Kafka ────────────────────────────────────────────
    GCN_NASA_CLIENT_ID: str
    GCN_NASA_CLIENT_SECRET: SecretStr
    GCN_NASA_ALERTS: list[str]

    # ── LiteLLM Proxy ────────────────────────────────────────
    LITELLM_BASE_URL: str = "http://localhost:4000/v1"
    LITELLM_API_KEY: SecretStr  # Lido de LITELLM_API_KEY no .env (mesmo valor que LITELLM_MASTER_KEY no docker/.env)
    LLM_MODEL_CLASSIFIER: str = "nasa-classifier"
    LLM_MODEL_EMBEDDER: str = "nasa-embedder"
    LLM_MODEL_FAST: str = "nasa-fast"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # Ignora variáveis extras no .env não declaradas nesta classe
    )
