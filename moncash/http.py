import requests
import datetime
from base64 import encodebytes
import json 

from moncash.constants import API 
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
        return status not in [200, 202, 201, 204, 422]

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

        self.__access_token = {"token":None, "taken_date":None}
    
    def __get_access_token(self):

        auth_string = b"Basic "+encodebytes(
            self.config.client_id.encode('ascii')+b":"+self.config.client_secret.encode('ascii')
        ).replace(b"\n", b"").strip()

        headers = {
            "Accept":"application/json",
            "Content-Type":"application/json",
            "Authorization": auth_string
        }

        resp = self.post(API[self.config.api_version]["auth"], headers_override=headers)

        access_token = resp["access_token"]

        self.__access_token["token"] =  'Bearer '+access_token
        self.__access_token["taken_date"] = datetime.datetime.now()

        return self.__access_token["token"]

    
    def __authorization_header(self):
        # check if we have an access token 
        if self.__access_token["token"]:
            # check if this access token is valid 
            if datetime.datetime.now() - self.__access_token["taken_date"] < 59:
                return self.__access_token["token"]
        
        return self.__get_access_token()

    def post(self, endpoint, payload=None, headers_override=None):
        params = {"scope":"read,write", "grant_type":"client_credentials"}

        if headers_override:
            headers = headers_override
        else:
             headers = {
                "Accept":"application/json",
                "Content-Type":"application/json",
                "Authorization":self.__authorization_header()
            }
        
        try:
            resp = requests.post(
                    self.config.base_url()+endpoint, 
                    params=params, 
                    headers=headers,
                    data=json.dumps(payload)
                )
        except Exception as e:
            pass

        try:
            resp_json = json.loads(resp.content.decode('utf-8'))
        except Exception as e:
            raise Exception("Unexpected Error")

        if self.is_error_status(resp.status_code):
            self.raise_exception_from_status(resp.status_code)
 
        return resp_json
        


       
        

    


    
    
    



