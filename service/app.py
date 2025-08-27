from fastapi import FastAPI, HTTPException
from .schemas import EventIn, Ack
from .sink import write_record

app = FastAPI(title="Stillfront Intake")

@app.get("/status")
def healthz():
    return {"status": "ok"}

@app.post("/collect", response_model=Ack, status_code=201)
def collect(evt: EventIn):
    if evt.event_type == "install" and not evt.device_id:
        raise HTTPException(status_code=422, detail="device_id required for install")
    if evt.event_type == "purchase":
        if not evt.currency or evt.amount is None:
            raise HTTPException(status_code=422, detail="currency and amount required for purchase")
    rec_id = write_record(evt.dict())
    return Ack(status="ok", id=rec_id)