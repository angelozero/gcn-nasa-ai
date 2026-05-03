from datetime import datetime

from pydantic import BaseModel, Field

from gcn_nasa_ai.models.base import GCNBase


class GCNLocalization(BaseModel):
    """Mapeia o core/Localization.schema.json"""

    ra: float = Field(ge=0, le=360, description="Right Ascension (deg)")
    dec: float = Field(ge=-90, le=90, description="Declination (deg)")
    ra_dec_error: float = Field(description="Uncertainty radius (deg)")


class EinsteinProbeWXTAlert(GCNBase, GCNLocalization):
    """
    Representa um alerta do Wide-field X-ray Telescope (WXT) da Einstein Probe.
    Focado na detecção de transientes rápidos em raios-X.
    """

    instrument: str = Field("WXT", frozen=True)
    trigger_time: datetime

    # O ID na Einstein Probe pode vir como uma lista de strings
    id: list[str]

    # Propriedades da Imagem e Detecção
    image_energy_range: tuple[float, float] = Field(
        ..., description="Faixa de energia da imagem em keV (ex: 0.5 a 4 keV)"
    )
    net_count_rate: float = Field(
        ..., description="Taxa de contagem líquida (counts/s)"
    )
    image_snr: float = Field(..., description="Signal-to-Noise Ratio da imagem")

    additional_info: str | None = None
