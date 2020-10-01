import moncash

gateway = moncash.MoncashGateway(
    client_id="12",
    secret_key="1aws34fggt"
)

payement = gateway.create_payement(
    amount="1000",
    order_id="12"
)

get_paid = payement.url

# TODO:  redirect the user to the payement url 
    
