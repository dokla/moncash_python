from tests.test_helper import *
from moncash.exceptions.request_timeout_error import *

class TestHttp(unittest.TestCase):
    @raises(RequestTimeoutError)
    def test_raise_exception_from_request_timeout(self):
        pass 
