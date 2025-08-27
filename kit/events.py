from datetime import datetime, timezone

def _utc_iso():
    return datetime.now(timezone.utc).isoformat()

class AppInstall:
    def __init__(self, device_id, user_id=None, campaign=None, app_version=None, ts=None):
        self.event_type = "install"
        self.device_id = device_id
        self.user_id = user_id
        self.campaign = campaign
        self.app_version = app_version
        self.ts = ts or _utc_iso()

    def to_dict(self):
        return self.__dict__

class PurchaseTxn:
    def __init__(self, device_id, currency="USD", amount_minor=0, item_id=None, quantity=1, user_id=None, app_version=None, ts=None):
        self.event_type = "purchase"
        self.device_id = device_id
        self.currency = currency
        self.amount_minor = int(amount_minor)
        self.item_id = item_id
        self.quantity = int(quantity)
        self.user_id = user_id
        self.app_version = app_version
        self.ts = ts or _utc_iso()

    def to_dict(self):
        return self.__dict__