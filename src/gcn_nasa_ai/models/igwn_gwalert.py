from pydantic import BaseModel, HttpUrl


class Classification(BaseModel):
    """Classificação probabilística do evento gravitacional."""

    BBH: float
    BNS: float
    NSBH: float
    Terrestrial: float


class Properties(BaseModel):
    """Propriedades físicas inferidas do evento."""

    HasMassGap: float
    HasNS: float
    HasRemnant: float


class Event(BaseModel):
    """Dados do evento gravitacional detectado."""

    central_frequency: float | None = None
    classification: Classification
    duration: float | None = None
    far: float
    group: str
    instruments: list[str]
    pipeline: str
    properties: Properties
    search: str
    significant: bool
    time: str


class GWAlert(BaseModel):
    """Representa um alerta de onda gravitacional do IGWN."""

    alert_type: str
    event: Event
    superevent_id: str
    time_created: str
    urls: dict[str, HttpUrl]
    external_coinc: dict | None = None
