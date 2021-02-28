import moncash

gateway = moncash.Moncash(
        client_id="26c0da72fb39f2219066e793663e133a",
        client_secret="eDW4R0KpN8UYQheoEX_OBwAztXqewARKbKevjwdkzm1gLlGGouzdv1znWpLNhuJ_",
        environment=moncash.environment.Sandbox
    )

get_paid_url = gateway.payment.create(
    amount=1000,
    reference=12
)

print(get_paid_url)

# TODO:  in your app redirect the user to the payment url to get paid
    
