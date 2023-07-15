from pydantic import BaseModel


class Sector(BaseModel):
    sector_id: str
    name: str
    type: str
    location: str
    projects: list
    workers: list
    administrators: list
