from pydantic.main import BaseModel


class Device(BaseModel):
    nome: str
    latitude: float
    longitude: float
