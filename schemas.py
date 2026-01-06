from pydantic import BaseModel, HttpUrl, field_validator
from .validators import reject_local_and_private_hosts


class WebsiteIn(BaseModel):
    website: HttpUrl  # Requires http/https and a hostname with a TLD

    @field_validator("website")
    @classmethod
    def validate_website_host(cls, v: HttpUrl):
        # v is a Pydantic URL type; v.host gives hostname without scheme/port
        reject_local_and_private_hosts(v.host)
        return v
