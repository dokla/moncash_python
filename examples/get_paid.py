import moncash

gateway = moncash.MonCashGateway(
    client_id="12",
    secret_key="1aws34fggt",
    environment=moncash.environment.Sandbox
)


payement = gateway.create_payement(
    amount="1000",
    order_id="12"
)

get_paid = payement.url

# TODO:  in your app redirect the user to the payement url to get paid
    
