from kit import Client, AppInstall, PurchaseTxn

def main():
    cli = Client(base_url="http://localhost:8080")

    print("install …")
    r1 = cli.send(AppInstall(device_id="dev-1", user_id="u1", campaign="promo"))
    print("  ->", r1.status_code, r1.json())

    print("purchase …")
    r2 = cli.send(PurchaseTxn(device_id="dev-1", currency="EUR", amount_minor=299, item_id="coins_300"))
    print("  ->", r2.status_code, r2.json())

    print("\nCheck ./.out/stream_debug.jsonl")

if __name__ == "__main__":
    main()