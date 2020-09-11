import hashlib

mystring = input('Bitte Text eingeben: ')
hash_object = hashlib.sha1(mystring.encode())

print(hash_object.hexdigest())