import requests
from moncash.contants import API 
from moncash.exceptions import (
                                    AuthenticationError, 
                                    AuthorizationError, 
                                    NotFoundError, 
                                    RequestTimeoutError, 
                                    UpgradeRequiredError, 
                                    TooManyRequestsError,
                                    ServerError, 
                                    ServiceUnavailableError, 
                                    GatewayTimeoutError, 
                                    UnexpectedError
                                )


class Http(object):

    @staticmethod
    def is_error_status(status):
        return status not in [200, 201, 204, 422]

    @staticmethod
    def raise_exception_from_status(status, message=None):
        if status == 401:
            raise AuthenticationError()
        elif status == 403:
            raise AuthorizationError(message)
        elif status == 404:
            raise NotFoundError()
        elif status == 408:
            raise RequestTimeoutError()
        elif status == 426:
            raise UpgradeRequiredError()
        elif status == 429:
            raise TooManyRequestsError()
        elif status == 500:
            raise ServerError()
        elif status == 503:
            raise ServiceUnavailableError()
        elif status == 504:
            raise GatewayTimeoutError()
        else:
            raise UnexpectedError("Unexpected HTTP_RESPONSE " + str(status))


    def __init__(self, config, environment=None):
        self.config = config
        self.environment = environment or self.config.environment 

        self.__access_token = None

    def post(self, endpoint, params=None, headers_override=None):
        headers = {
            "Accept":"application/json",
            "Authorization":self.__authorization_header()
        }

        if headers_override:
            headers = headers_override

        try:
            r = requests.post(
                    self.config.base_url()+endpoint, 
                    params=params, 
                    headers=headers,
                    request_body=request_body
                )
        except Exception as e:
            print(e)
    
    def __get_access_token(self):
        if self.__access_token:
            return self.__access_token 
        
        params = {"scope":"read,write", "grant_type":"client_credentials"}
        resp = self.post(self, API[self.config.version]["auth"], )
    
    
    



