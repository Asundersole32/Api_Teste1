from pydantic import BaseModel


class Worker(BaseModel):
    id: str
    name: str
    age: int
    address: str
    salary: float


class Administrator(BaseModel):
    worker_id: Worker
    adm_level: int | None = 1


class Engineers(BaseModel):
    worker_id: Worker
    training: str
    training_location: str


class Common(BaseModel):
    worker_id: Worker
    occupation: str
