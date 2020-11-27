from moncash.exceptions import ConfigurationError
from moncash.environment import Environment 

class Configuration(object):
    def __init__(self, environment=None, client_id=None, client_secret=None):

        if not isinstance(client_id, int):
            raise ConfigurationError("ConfigurationError: missing client_id or it is not an integer")

        if not isinstance(client_secret, str): 
            raise ConfigurationError("ConfigurationError: missing client_secret or it is not a string")

        if not isinstance(environment, Environment):
            raise ConfigurationError("ConfigurationError: missing value environment or it is not an environment")

        self.environment = environment
        self.client_id = client_id
        self.client_secret = client_secret
    