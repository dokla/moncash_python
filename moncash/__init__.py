
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
    >>> gateway = moncash.Moncash(client_id='', client_secret='')
    >>> payement = gateway.payement
    >>> payement.create(amount=500, to='+50948438330')


:copyright: (c) 2020 by Madsen Servius.
:license: Apache 2.0, see LICENSE for more details.
"""


from .gateway import Moncash 
from .configuration import Configuration 