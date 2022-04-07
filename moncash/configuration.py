from moncash.http import Http

class Configuration(object):
    def __init__(self, client_id=None, client_secret=None, environment=None):

        self.client_id = client_id
        self.client_secret = client_secret
        self.environment = environment

        self.api_version = "v1"
    
    def http(self):
        return Http(self)
    
    def base_url(self):
        return self.environment.protocol+self.environment.host
    