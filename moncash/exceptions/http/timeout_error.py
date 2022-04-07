from moncash.exceptions.unexpected_error import UnexpectedError 

class TimeoutError(UnexpectedError):
    pass

class ConnectTimeoutError(TimeoutError):
    pass

class ReadTimeoutError(TimeoutError):
    pass