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

    from moncash.exceptions import MoncashError

    gateway = moncash.Moncash(
        client_id="xxxxxxxx",
        client_secret="xxxxxxxx",
        # in production: environment = moncash.environment.Production
        environment=moncash.environment.Sandbox
    )

    # YOU SHOULD HANDLE ERROR
    try:
        get_paid_url = gateway.payment.create(amount=250, reference=10)
    except MoncashError:
        get_paid_url = None
        print("Unexpected error...")
        
    
    print(get_paid_url)

    # TODO: redirect the user to get_paid_url
```

### Query transactions status

#### Query the transactions status

```python

    import moncash 

    from moncash.exceptions import MoncashError, NotFoundError

    gateway = moncash.Moncash(
        client_id="xxxxxxxx",
        client_secret="xxxxxxxx",
        # in production: environment = moncash.environment.Production
        environment=moncash.environment.Sandbox
    )

    # YOU SHOULD HANDLE ERROR
    try:
        # To retrieve the payment with the transaction Id 
        # you should use: gateway.payment.get_by_id(id)
        response = gateway.payment.get_by_ref(reference=10)
    except NotFoundError:
        response = None
        print("We did found this transaction... not valid")
    except MoncashError:
        response = None
        print("Unexpected error...")
        
    
    print(response)

    # TODO: redirect the user to get_paid_url
```

The response should be something like:

```json
    {
        "reference": "13", 
        "transaction_id": "2160048483", 
        "cost": "250", 
        "message": "successful", 
        "payer": "50936050083"
    }
```


