# -*- coding: utf-8 -*-
"""
Created on Wed May 27 10:05:53 2020

@author: dw

Identifizieren des Passwortes welches zum angegebenen SHA256 HASH gehört.
"""

import hashlib

password_hash = "112aa01926aebb65c5e09cc0a25ce2b5cff2ec5df0e9b123510db6753557e552"
extra_chars = "!$%&/()=?"

with open("./Kursmaterialien/data/dictionary.txt", "r") as file:
    for line in file:
        word = line.strip()
        
        for char in extra_chars:
            w1 = word + char
            
            for char2 in extra_chars:
                w2 = w1 + char2
        
                if hashlib.sha256(w2.encode()).hexdigest() == password_hash:
                    print(word + char + char2)

print("Programm fertig!")