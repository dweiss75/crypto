# -*- coding: utf-8 -*-
"""
Created on Thu May 28 16:13:14 2020

@author: dw
"""


#!/usr/bin/python3
entry = "Gast:$6$QIDRtc2VvLRpaLvx$yzGEFkIh970o45MEV92ICCus3KBRwVi82y/tgBOHsY0Cgl2qjXqOe98jGcITIoRenqyyE8HXZllJj2KoaMSBZ/:18410:0:99999:7:::"
password_hash ="$6$QIDRtc2VvLRpaLvx$yzGEFkIh970o45MEV92ICCus3KBRwVi82y/tgBOHsY0Cgl2qjXqOe98jGcITIoRenqyyE8HXZllJj2KoaMSBZ/"
salt = "$6$QIDRtc2VvLRpaLvx$"




import crypt

with open("password-crack-dictionary.txt", "r") as file:
	for line in file:
		word = line.strip()
		if crypt.crypt(word, salt) == password_hash:
			print(word)
print("Programm fertig!")