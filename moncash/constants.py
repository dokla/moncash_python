
BASE = "moncashbutton.digicelgroup.com"

SANDBOX_HOST = f"sandbox.{BASE}/Api"

PROD_HOST = f"api.{BASE}"

SANDBOX_REDIRECT_URL = f"https://sandbox.{BASE}/Moncash-middleware"
PROD_REDIRECT_URL = f"https://{BASE}/Moncash-middleware"

API = {
    "v1": {
        "auth": "/oauth/token",
        "create_payment": "/v1/CreatePayment",
        "get_payment_by_id": "/v1/RetrieveTransactionPayment",
        "get_payment_by_ref": "/v1/RetrieveOrderPayment"
    }
}