from pydantic import BaseModel, Field, validator

class Stat(BaseModel):
    id: str
    open_price: float = Field(..., description="Ціна відкриття торгівельної пари")
    close_price: float = Field(..., description="Ціна закриття торгівельної пари")
    high_price: float = Field(..., description="Найвища ціна торгівельної пари за період")
    low_price: float = Field(..., description="Найнижча ціна торгівельної пари за період")
    volume: float = Field(..., description="Загальний обсяг угод для торгівельної пари")
    last_trade_id: int
    volume_24h: float
    volume_30d: float
    best_bid: float
    best_ask: float
    side: str
    time: str
    trade_id: int
    last_size: float
    sequence: int
    product_id: str
    time_24h: str

    @validator("side")
    def validate_side(cls, v):
        if v not in {"buy", "sell"}:
            raise ValueError("Сторона повинна бути 'buy' або 'sell'")
        return v
    
    @validator("open_price", "close_price", "high_price", "low_price", "volume", pre=True)
    def convert_to_float(cls, value: str) -> float:
        return float(value)
