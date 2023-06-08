# https://www.tutorialspoint.com/md5-hash-encoding-using-python


''' 1. The Script takes an input, passes it to hashlib md5 to hash
    2. opens a text file containing hashes.
    3. The for loop compares the hashes in the .txt file to the hash result of the input and checks for
       a match. '''

import hashlib


# input to be hashed
mystring = input('Enter string to hash: ') 
hash_obj = hashlib.md5(mystring.encode())

# print(hash_obj.hexdigest())
# hash number
hash = hash_obj.hexdigest() 
print(f'hash/finger_print: {hash}')

f = open("c:/Users/ursos/Desktop/School/Thonny Progs/Cryptography/Hashes/hashes.txt", "r")

for i in f:
    if i.strip('\n') == hash:
        print(f'HASH FOUND!!!: {mystring} = {hash}')
        break
    
f.close()


