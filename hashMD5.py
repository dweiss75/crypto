import hashlib

mystring = input('Bitte Text eingeben: ')
hash_object = hashlib.md5(mystring.encode())
print(hash_object.hexdigest())

