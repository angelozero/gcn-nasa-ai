from datetime import datetime

from pydantic import Field

from app.models.base import GCNBase


class GCNHeartbeat(GCNBase):
    """
    Representa o sinal de heartbeat do sistema GCN.
    Utilizado para monitoramento de saúde da conexão e rastreamento de latência.
    """

    alert_datetime: datetime = Field(
        description="Timestamp ISO 8601 indicando quando o heartbeat foi gerado."
    )

    def time_since_alert(self) -> float:
        """Retorna a latência em segundos desde a geração do alerta."""
        now = datetime.now(self.alert_datetime.tzinfo)
        return (now - self.alert_datetime).total_seconds()
