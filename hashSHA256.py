import hashlib

mystring = input('Bitte Text eingeben: ')
hash_object = hashlib.sha256(mystring.encode())
print(hash_object.hexdigest())
