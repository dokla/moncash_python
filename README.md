# moncash_python
Simple python wrapper to perform and retrieve payment to moncash api with python

## Features
* Receive money from a mobile account to business account 
* Query transaction status

## Quickstart 

### Installation

#### Using pip

```
    pip install moncash
```

### Receive money from a mobile account 
```python

import moncash 

gateway = moncash.Moncash(
    client_id="xxxxxxxx",
    client_secret="xxxxxxxx",
    environment=moncash.environment.Sandbox
)

# you should handle error
try:
    get_paid_url = gateway.payment.create(amount=250, reference=10)
except moncash.exceptions.MoncashError:
    get_paid_url = None
    print("Unexpected error...")
    

print(get_paid_url)

# TODO: redirect the user to get_paid_url
```

### Query transactions status

#### Query the transactions status

Grab transaction with the reference

```python

....

# you should handle error
try:
    response = gateway.payment.get_by_ref(reference=10)
except moncash.exceptions.NotFoundError:
    response = None
    print("We didnt found this transaction... It is not valid")
except moncash.exceptions.MoncashError:
    response = None
    print("Unexpected error...")

```

Grab transaction with the transactionId

```python

....

# you should handle error
try:
    response = gateway.payment.get_by_id(transactionId=10)
except moncash.exceptions.NotFoundError:
    response = None
    print("We didnt found this transaction... It is not valid")
except moncash.exceptions.MoncashError:
    response = None
    print("Unexpected error...")

```

The response should be something like for the transactions querying status (whether with reference or the id):

```json
{
    "reference": "13", 
    "transaction_id": "2160048483", 
    "cost": "250", 
    "message": "successful", 
    "payer": "50936050083"
}
```

## Exceptions 

> A good application is an application where you care about errors
> (Madsen Servius)

Exhaustive list of the Exceptions:

* MoncashError 
* ConfigurationError 
* PaymentError
* AuthenticationError 
* AuthorizationError 
* GatewayTimeoutError 
* RequestTimeoutError
* ServerError
* ServiceUnavailableError
* TooManyRequestsError
* UnexpectedError
* UpgradeRequiredError
* NotFoundError
* ConnectionError 
* InvalidResponseError 
* TimeoutError
* ConnectTimeoutError
* ReadTimeoutError

To import them in you code you have to write:

    from moncash.exceptions import NameOfTheExceptionCatched


## Authors

Madsen Servius (madsen@dokla.ht)

