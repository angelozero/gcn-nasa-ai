from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from app.models.base import GCNBase


class GCNAlertCore(BaseModel):
    """Mapeia o esquema core/Alert.schema.json."""

    mission: str
    instrument: str | None = None
    messenger: Literal["GW", "EM", "Neutrino", "Cosmic Ray"]
    alert_datetime: datetime
    alert_type: str
    id: str


class GCNLocalization(BaseModel):
    """Mapeia o esquema core/Localization.schema.json."""

    ra: float = Field(ge=0, le=360)
    dec: float = Field(ge=-90, le=90)
    ra_dec_error: float | None = None


class DSA110FRBNotice(GCNBase, GCNAlertCore, GCNLocalization):
    """
    Modelo final para o DSA-110, herdando a estrutura unificada de alertas NASA
    e adicionando campos específicos da missão.
    """

    model_config = ConfigDict(populate_by_name=True)

    event_name: str | None = None
    trigger_time: datetime | None = None
    record_number: int | None = None

    # Campos customizados do exemplo fornecido
    example_field_1: str | None = Field(None, description="Texto customizado da missão")
    example_field_2: int | None = Field(None, description="Número customizado da missão")
