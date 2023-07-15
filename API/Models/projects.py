from pydantic import BaseModel


class Projects(BaseModel):
    project_id: str
    name: str
    client: str
    type: str
    price: float
