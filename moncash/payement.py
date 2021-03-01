from moncash.constants import API 
from moncash.exceptions import PaymentError 

class Payment(object):
    def __init__(self, gateway):
        self.gateway = gateway
        self.config = gateway.config
    
    def __post(self, endpoint, payload):
        return self.config.http().post(endpoint, payload)
    
    def create(self, amount, reference):
        if amount == 0:
            raise PaymentError("Payment amount can not be zero")
        
        response = self.__post(
            endpoint = API[self.config.api_version]["create_payment"],
            payload = {
                "amount":amount,
                "orderId":reference
            } 
        )

        self.url = self.config.environment.redirect_url+"/Payment/Redirect?token="+response["payment_token"]["token"]

        return self.url

    
    def get_by_ref(self, reference):
        response = self.__post(
            endpoint=API[self.config.api_version]["get_payment_by_ref"],
            payload={
                    "orderId":reference
                }
        )

        return response

    
    # def get_by_id(self, transactionId):
    #     response = self.__post(
    #         endpoint=API[self.config.api_version]["get_payment_by_id"],
    #         payload={
    #                 "transactionId":transactionId
    #             }
    #     )

    #     return response



