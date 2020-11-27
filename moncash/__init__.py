
"""
                                  _     
  /\/\   ___  _ __   ___ __ _ ___| |__  
 /    \ / _ \| '_ \ / __/ _` / __| '_ \ 
/ /\/\ \ (_) | | | | (_| (_| \__ \ | | |
\/    \/\___/|_| |_|\___\__,_|___/_| |_|
                                        

This is an unofficial wrapper providing convenient access to 
the MonCash API for applications written in Python

Basic usage:

    >>> import moncash
    >>> gateway = moncash.MoncashGateway(client_id='', client_secret='', env='')
    >>> get_paid = gateway.get_paid(amount=500, order_id=205)
    >>> get_paid.url



:copyright: (c) 2020 by Madsen Servius.
:license: Apache 2.0, see LICENSE for more details.
"""


from .gateway import MoncashGateway
from .configuration import Configuration 
from .environment import Environment
