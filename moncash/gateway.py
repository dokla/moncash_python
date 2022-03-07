
"""
                                  _     
  /\/\   ___  _ __   ___ __ _ ___| |__  
 /    \ / _ \| '_ \ / __/ _` / __| '_ \ 
/ /\/\ \ (_) | | | | (_| (_| \__ \ | | |
\/    \/\___/|_| |_|\___\__,_|___/_| |_|
                                        

This is an unofficial wrapper providing convenient access to 
the MonCash API for applications written in Python

:copyright: (c) 2020-2022 by DOKLA.
:license: Apache 2.0, see LICENSE for more details.
"""


from moncash.configuration import Configuration
from moncash.payment import Payment

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
        

if __name__ == '__main__':
    print("__package__")
    
        


    

