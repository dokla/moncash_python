from moncash import MoncashGateway

gateway = MoncashGateway(
    client_id="xxxxxxxxxxxxxx",
    secret_key="xxxxxxxxxxxxx",
    environment=moncash.environment.Sandbox
)

payment_gateway = gateway.payment

url = payment_gateway.create(
    amount="1000",
    reference="12"
)

print(url)

# TODO:  in your app redirect the user to the payement url to get paid
    
