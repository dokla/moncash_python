from moncash import constants

class Environment(object):
    
    def __init__(self, name, host):
        self.__name__ = name 
        self.host = host
        self.protocol = "https://"

        if name == 'Sandbox':
            self.redirect_url = constants.SANDBOX_REDIRECT_URL 
        elif name == 'Production':
            self.redirect_url = constants.PROD_REDIRECT_URL
        else:
            raise EnvironmentError("Environment should be named 'Sandbox' or 'Production'")
        

Sandbox = Environment('Sandbox', constants.SANDBOX_HOST)

Production = Environment('Production', constants.PROD_HOST)
