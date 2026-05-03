from datetime import datetime, timezone

from pydantic import BaseModel, ConfigDict, Field, field_validator


class GCNCircular(BaseModel):
    """Representa uma circular do sistema GCN."""

    model_config = ConfigDict(populate_by_name=True)

    circular_id: int = Field(alias="circularId")
    event_id: str = Field(alias="eventId")
    format: str
    subject: str
    created_on: datetime = Field(alias="createdOn")
    submitter: str
    body: str
    submitted_how: str = Field(alias="submittedHow")

    @field_validator("created_on", mode="before")
    @classmethod
    def transform_milliseconds_to_datetime(cls, v: int | float | str) -> datetime | str:
        """
        Converte timestamps em milissegundos (comuns em APIs de Astronomia)
        para objetos datetime timezone-aware do Python.
        """
        if isinstance(v, (int, float)):
            return datetime.fromtimestamp(v / 1000.0, tz=timezone.utc)
        return v
