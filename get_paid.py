import moncash

gateway = moncash.Moncash(
        client_id="26c0da72fb39f2219066e793663e133a",
        client_secret="eDW4R0KpN8UYQheoEX_OBwAztXqewARKbKevjwdkzm1gLlGGouzdv1znWpLNhuJ_",
        environment=moncash.environment.Sandbox
    )

# get_paid_url = gateway.payment.create(
#     amount=2250,
#     reference=14
# )

# print(get_paid_url)

resp = gateway.payment.get_by_ref(13)

print(resp)


# TODO:  in your app redirect the user to the payment url to get paid
    
