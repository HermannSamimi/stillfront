import os, json, uuid

LOG_DIR = ".output"
LOG_FILE = "stream_debug.json"

def write_record(record: dict) -> str:
    rec_id = str(uuid.uuid4())
    os.makedirs(LOG_DIR, exist_ok=True)

    path = os.path.join(LOG_DIR, LOG_FILE)

    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    entry = {"id": rec_id, "record": record}
    data.append(entry)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    return rec_id