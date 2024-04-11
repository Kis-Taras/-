from pydantic import BaseModel, validator
from typing import List, Optional


class Candle(BaseModel):
    timestamp: int
    low: float
    high: float
    open: float
    close: float
    volume: float

class HistoricalData(BaseModel):
    pair: str
    begin: int
    end: int
    granularity: int = 60
    data: List[Candle]

    @validator('pair', 'begin', 'end')
    def check_empty(cls, v):
        if v.strip() == "":
            raise ValueError("Field cannot be empty")
        return v

    @validator('granularity')
    def check_granularity(cls, v):
        if v not in [60, 300, 900, 3600, 21600, 86400]:
            raise ValueError("Granularity must be one of: 60, 300, 900, 3600, 21600, 86400")
        return v

    @validator('begin', 'end')
    def check_non_negative(cls, v):
        if v < 0:
            raise ValueError("Value must be non-negative")
        return v
