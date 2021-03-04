# moncash_python
Simple python wrapper to perform and retrieve payment to moncash api with python

## Features
* Receive money from a mobile account to business account
* Send money from business account to mobile account 
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
        environment=moncash.environment.Sandbox
        # in production: environment = moncash.environment.Production
    )

    # You should handle error
    # It can be any kind of error
    # AuthenticationError, ServerError, etc...
    # but all errors are inherited from MoncasError
    try:
        get_paid_url = gateway.payment.create(
            amount=250,
            reference=10
        )
    except MoncashError:
        print("Unexpected error...")
    
    print(get_paid_url)

    # TODO: redirect the user to get_paid_url
```

### Send money from business account to mobile account 

### Query Status


