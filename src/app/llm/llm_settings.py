from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class LLMSettings(BaseSettings):
    """Configurações exclusivas do cliente LLM (proxy LiteLLM).

    Carregadas automaticamente do arquivo .env — sem dependência de
    GCNNasaSettings ou qualquer outra configuração da aplicação.
    """

    LITELLM_BASE_URL: str = "http://localhost:4000/v1"
    # Mesmo valor que LITELLM_MASTER_KEY definido no docker/.env
    LITELLM_API_KEY: SecretStr

    model_config = SettingsConfigDict(
        env_file=[".env", "../.env"],
        env_file_encoding="utf-8",
        extra="ignore",
    )
