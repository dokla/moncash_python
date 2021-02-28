from moncash.configuration import Configuration
from moncash.payement import Payment

class Moncash(object):

    def __init__(self, config=None, **kwargs):
        if isinstance(config, Configuration):
            self.config = config 
        else:
            self.config = Configuration(
                client_id=kwargs.get("client_id"),
                client_secret=kwargs.get("client_secret"),
                environment=kwargs.get("environment")
            ) 
        self.payment = Payment(self)
        

    
        


    

