import requests

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
    

    def post(self):
        pass
    
    def get(self):
        pass 
    
    def put(self):
        pass
    
    def delete(self):
        pass 
    
    def _make_request(self):
        pass

    



