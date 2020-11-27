class TransactionGateway(object):
    def __init__(self, gateway, order_id):
        self.gateway = gateway 
        self.config = self.gateway.config
        self.order_id = order_id 
