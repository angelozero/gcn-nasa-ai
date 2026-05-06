from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

# Tipos de eventos astronômicos reconhecidos pelo pipeline de classificação
KNOWN_TYPES: frozenset[str] = frozenset(
    {"GRB", "GW", "FRB", "NEUTRINO", "X-RAY", "SUPERNOVA"}
)


class GCNNasaSettings(BaseSettings):
    """Configurações do consumidor GCN NASA carregadas do arquivo .env.

    Responsabilidade única: credenciais e parâmetros do Kafka GCN.
    Configurações do LLM ficam em LLMSettings (llm/llm_settings.py).
    Aliases de modelos ficam em LLMModels (config/llm_models.py).
    """

    # ── GCN Kafka ────────────────────────────────────────────
    GCN_NASA_CLIENT_ID: str
    GCN_NASA_CLIENT_SECRET: SecretStr
    GCN_NASA_ALERTS: list[str]
    # Tempo total (em segundos) que o consumidor ficará ativo escutando mensagens
    CONSUMER_DURATION: int = 30
    INDEX_NAME: str

    model_config = SettingsConfigDict(
        # Tenta carregar do diretório atual, ou um nível acima
        env_file=[".env", "../.env"],
        env_file_encoding="utf-8",
        extra="ignore",
    )
