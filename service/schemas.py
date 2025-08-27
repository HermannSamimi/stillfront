from pydantic import BaseModel
from typing import Optional

class EventIn(BaseModel):
    event_type: str
    device_id: str
    user_id: Optional[str] = None
    app_version: Optional[str] = None
    ts: Optional[str] = None
    campaign: Optional[str] = None
    currency: Optional[str] = None
    amount_minor: Optional[int] = None
    item_id: Optional[str] = None
    quantity: Optional[int] = 1

class Ack(BaseModel):
    status: str
    id: str