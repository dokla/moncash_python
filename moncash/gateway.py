from .configuration import Configuration
from .get_paid import GetPaidGateway
from .transaction import TransactionGateway

class MoncashGateway(object):

    def __init__(self, config=None, **kwargs):
        if isinstance(config, Configuration):
            self.config = config 
        else:
            self.config = Configuration(
                client_id=kwargs.get("client_id"),
                client_secret=kwargs.get("client_secret"),
                environment=kwargs.get("environment")
            ) 

    def create_payement(self, amount, order_id):
        return GetPaidGateway(self, amount, order_id)
        
    def get_transaction(self):
        return TransactionGateway(self, order_id)
        


    

