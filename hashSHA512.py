# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 10:17:54 2018

@author: dw
"""

import hashlib

mystring = input('Bitte Text eingeben: ')
hash_object = hashlib.sha512(mystring.encode())
print(hash_object.hexdigest())