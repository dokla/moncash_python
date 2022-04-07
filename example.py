import moncash

gateway = moncash.Moncash(
    client_id="fa36258cf6ff7f0e82ba52a859808382",
    client_secret="PAZORCbzs28eE2sQdWQ9ynAAk-inYP-uSWILraU3CWRyO1mnbb050T3j_rUm8cRp",
    environment=moncash.environment.Production
)

get_paid_url = None 

try:
    get_paid_url = gateway.payment.capture(amount=250, reference=78)
except moncash.exceptions.MoncashError as err:
    print(err)

print(get_paid_url)