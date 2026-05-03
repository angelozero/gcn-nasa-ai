from datetime import datetime

from pydantic import Field

from gcn_nasa_ai.models.base import GCNBase


class GCNHeartbeat(GCNBase):
    """
    Representa o sinal de 'Heartbeat' do sistema GCN.
    Utilizado para monitoramento de saúde da conexão e latência.
    """

    alert_datetime: datetime = Field(
        description="ISO 8601 timestamp indicando quando o batimento foi gerado."
    )

    def time_since_alert(self) -> float:
        """Calcula a latência em segundos desde a geração do alerta."""
        now = datetime.now(self.alert_datetime.tzinfo)
        return (now - self.alert_datetime).total_seconds()
