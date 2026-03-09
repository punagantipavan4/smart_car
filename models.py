from pydantic import BaseModel

class Car(BaseModel):
  brand: str
  model: str
  year: int
  vechile_type: str
  price_per_day: float
  availbility: bool=True


