from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class GCNNasaSettings(BaseSettings):
    """Configurações centralizadas do GCN NASA carregadas do .env."""

    GCN_NASA_CLIENT_ID: str
    GCN_NASA_CLIENT_SECRET: SecretStr
    GCN_NASA_ALERTS: list[str]

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # Ignora outras variáveis no .env que não estão na classe
    )
