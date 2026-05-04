from datetime import datetime

from pydantic import BaseModel, Field

from app.models.base import GCNBase


class GCNLocalizationBase(BaseModel):
    """Mapeia o esquema core/Localization.schema.json."""

    ra: float = Field(ge=0, le=360)
    dec: float = Field(ge=-90, le=90)
    ra_dec_error: float | None = None


class CoincidentEventLocalization(GCNLocalizationBase):
    """Localização de um evento coincidente com probabilidade de contenção."""

    containment_probability: float
    systematic_included: bool


class IceCubeCoincidentEvent(BaseModel):
    """Evento coincidente detectado pelo IceCube."""

    event_dt: float = Field(description="Diferença de tempo em relação ao trigger")
    localization: CoincidentEventLocalization
    id: list[str]
    event_pval_generic: float
    event_pval_bayesian: float | None = None


class FluxSensitivityRange(BaseModel):
    """Faixa de sensibilidade de fluxo de neutrinos."""

    flux_sensitivity: list[float]
    sensitive_energy_range: list[float]


class IceCubeLVKNuTrackSearch(GCNBase):
    """
    Representa a busca de trilhas de neutrinos do IceCube correlacionada a eventos LVK.
    """

    type: str = Field("IceCube LVK Alert Nu Track Search", frozen=True)
    reference: dict[str, str] = Field(
        description="Referência ao alerta LVK original (ex: S230914ak)"
    )
    ref_ID: str
    alert_datetime: datetime
    trigger_time: datetime

    # Metadados da Observação
    observation_start: datetime
    observation_stop: datetime
    observation_livetime: float

    # Estatísticas de Coincidência
    pval_generic: float
    pval_bayesian: float | None = None
    n_events_coincident: int
    coincident_events: list[IceCubeCoincidentEvent]

    most_probable_direction: dict[str, float]
    neutrino_flux_sensitivity_range: FluxSensitivityRange
