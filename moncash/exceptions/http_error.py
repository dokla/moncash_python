from moncash.exceptions import MoncashError

class AuthenticationError(MoncashError):
    pass

class AuthorizationError(MoncashError):
    pass

class NotFoundError(MoncashError):
    pass 

class RequestTimeoutError(MoncashError):
    pass

class UpgradeRequiredError(MoncashError):
    pass
                                    
class TooManyRequestsError(MoncashError):
    pass
                                    
class ServerError(MoncashError):
    pass
                                    
class ServiceUnavailableError(MoncashError):
    pass
                                    
class GatewayTimeoutError(MoncashError):
    pass

class UnexpectedError(MoncashError):
    pass