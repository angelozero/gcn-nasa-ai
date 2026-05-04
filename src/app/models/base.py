from pydantic import BaseModel, ConfigDict, Field, HttpUrl


class GCNBase(BaseModel):
    """Metadados base compartilhados por todos os esquemas de alerta GCN."""

    model_config = ConfigDict(populate_by_name=True)
    schema_url: HttpUrl = Field(alias="$schema")
