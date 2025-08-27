from pydantic import BaseModel

class EventIn(BaseModel):
    event_type: str
    device_id: str | None = None
    user_id: str | None = None
    app_version: str | None = None
    currency: str | None = None
    amount: int | None = None
    ts: str | None = None

class Ack(BaseModel):
    status: str
    id: str