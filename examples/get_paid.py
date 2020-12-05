import moncash

moncash_gateway = moncash.Moncash(
        client_id="xxxxxxxxxxxxxx",
        secret_key="xxxxxxxxxxxxx",
        environment=moncash.environment.Sandbox
    )

payment_gateway = moncash_gateway.payment

get_paid_url = payment_gateway.create(
    amount="1000",
    reference="12"
)

print(get_paid_url)

# TODO:  in your app redirect the user to the payment url to get paid
    
