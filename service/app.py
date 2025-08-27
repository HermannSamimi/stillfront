from fastapi import FastAPI, HTTPException
from .schemas import EventIn, Ack
from .sink import write_record

app = FastAPI(title="PlayPulse Intake")

@app.get("/status")
def healthz():
    return {"status": "ok"}

@app.post("/collect", response_model=Ack, status_code=201)
def collect(evt: EventIn):
    # minimal checks
    if not evt.event_type or not evt.device_id:
        raise HTTPException(status_code=400, detail="event_type and device_id are required")

    if evt.event_type == "purchase":
        if evt.currency is None or evt.amount_minor is None:
            raise HTTPException(status_code=422, detail="currency and amount_minor are required for purchase")

    rec_id = write_record(evt.dict())
    return Ack(status="ok", id=rec_id)