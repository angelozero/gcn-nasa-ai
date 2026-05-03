from datetime import datetime
from typing import Literal

from pydantic import ConfigDict, Field

from gcn_nasa_ai.models.base import GCNBase


class CHIMEFRBNotice(GCNBase):
    """Representa um alerta de Fast Radio Burst detectado pelo CHIME."""

    model_config = ConfigDict(populate_by_name=True)

    alert_type: Literal["initial", "update", "retraction"]
    id: str
    description: str

    # Datas e Tempos
    trigger_time: datetime
    trigger_time_error: float
    trigger_time_inf_freq: datetime
    trigger_time_inf_freq_error: float

    # Dados Astrofísicos
    snr: float = Field(description="Signal-to-Noise Ratio")
    importance: float

    # Coordenadas e Erros
    ra: float = Field(description="Right Ascension (deg)")
    dec: float = Field(description="Declination (deg)")
    ra_dec_error: tuple[float, float, float]

    # Medida de Dispersão (DM)
    dm: float = Field(description="Dispersion Measure")
    dm_error: float
    dm_gal_ne_2001_max: float

    # Configurações do Instrumento
    sampling_time: float
    spectral_band: tuple[float, float]
    spectral_band_units: str
    npol: int
    tsys: float
