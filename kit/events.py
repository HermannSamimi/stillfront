from datetime import datetime, timezone

def _utc_iso():
    return datetime.now(timezone.utc).isoformat()

class AppInstall:
    def __init__(self, device_id, user_id=None, app_version=None, ts=None):
        self.event_type = "install"
        self.device_id = device_id
        self.user_id = user_id
        self.app_version = app_version
        self.ts = ts or _utc_iso()

    def to_dict(self):
        return self.__dict__

class PurchaseTxn:
    def __init__(self, currency="USD", amount=0, user_id=None, ts=None):
        self.event_type = "purchase"
        self.currency = currency
        self.amount = int(amount)
        self.user_id = user_id
        self.ts = ts or _utc_iso()

    def to_dict(self):
        return self.__dict__