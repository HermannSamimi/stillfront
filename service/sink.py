# try to stream, but if fails, data will be stored in a local JSON file
# simlation

import os, json, uuid, boto3

LOG_DIR = "output"
LOG_FILE = "stream_debug.json"
STREAM_NAME = os.getenv("FIREHOSE_STREAM", "stillfront-events-dev")

def write_record(event: dict) -> str:
    record_id = str(uuid.uuid4())
    item = {"id": record_id, "event": event}

    # tring to send to firehose if creds exist
    if boto3 and os.getenv("AWS_ACCESS_KEY_ID"):
        try:
            client = boto3.client("firehose")
            client.put_record(
                DeliveryStreamName=STREAM_NAME,
                Record={"Data": (json.dumps(item) + "\n").encode("utf-8")}
            )
            return record_id
        except Exception:
            pass

    os.makedirs(LOG_DIR, exist_ok=True)
    path = os.path.join(LOG_DIR, LOG_FILE)
    data = []
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            data = []
    data.append(item)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    return record_id