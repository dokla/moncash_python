from .http import Http 

class GetPaidGateway(object):
    def __init__(self, gateway, amount, order_id):
        self.gateway = gateway
        self.config = self.gateway.config
        self.amount = amount 
        self.order_id = order_id
    
    @property
    def url(self):
        pass