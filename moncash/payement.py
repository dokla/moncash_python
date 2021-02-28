from moncash.constants import API 
from moncash.exceptions import PaymentError 

class PaymentGateway(object):
    def __init__(self, gateway):
        self.gateway = gateway
        self.config = gateway.config
    
    def create(self, amount, reference):
        if amount == 0:
            raise PaymentError("Payment amount can not be zero")
        
        
        response = self._post(
            {
                "amount":amount,
                "orderId":reference
            }, 
            API[self.config.api_version]["create_payment"]
        )

        self.url = self.config.base_url()+response.token

        return self.url

    
    def find_by_ref(self, reference):
        response = self.__post(
            {
                "orderId":reference
            }, 
            API[self.config.api_version]["get_payment_by_ref"]
        )

        return response

    
    def find_by_id(self, transactionId):
        response = self.__post(
            {
                "transactionId":transactionId
            }, 
            API[self.config.api_version]["get_payment_by_id"]
        )

        return response

    
    def __post(self, data, endpoint):
        return self.config.http().post(endpoint, data)


