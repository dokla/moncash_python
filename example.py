import moncash

gateway = moncash.Moncash(
    client_id="xxxxxxxxxxxxxxxx",
    client_secret="xxxxxxxxxxxx",
    environment=moncash.environment.Production
)

get_paid_url = None 

try:
    get_paid_url = gateway.payment.capture(amount=250, reference=78)
except moncash.exceptions.MoncashError as err:
    print(err)

print(get_paid_url)