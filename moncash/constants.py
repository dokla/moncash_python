
BASE = "moncashbutton.digicelgroup.com"

SANDBOX_HOST = f"sandbox.{BASE}/Api"

PROD_HOST = f"{BASE}/Api"

SANDBOX_REDIRECT_URL = f"https://sandbox.{BASE}/Moncash-middleware"
PROD_REDIRECT_URL = f"https://{BASE}/Moncash-middleware"

API = {
    "v1": {
        "auth": "/oauth/token",
        "create_payment": "/v1/CreatePayment",
        "transfert":"v1/Transfert",
        "get_payment_by_id": "/v1/RetrieveTransactionPayment",
        "get_payment_by_ref": "/v1/RetrieveOrderPayment"
    }
}