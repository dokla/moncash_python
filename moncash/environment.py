from moncash import constants

class Environment(object):
    
    def __init__(self, name, server):
        self.__name__ = name 
        self.server = server 



Sandbox = Environment('Sandbox', constants.SANDBOX)

Production = Environment('Production', constants.PRODUCTION)
