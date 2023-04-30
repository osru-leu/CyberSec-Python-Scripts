

import hashlib
import random



def process_hashes(hash):

    hash_str = str(hash)
    salt = str(random.randint(409, 1009))
    salted = salt + hash_str
    hash_obj = hashlib.md5(salted.encode())
    finger_print = hash_obj.hexdigest()
    
    return salt, finger_print




if __name__ == "__main__":  

    hash_f = open("c:/Users/ursos/Desktop/School/Thonny Progs/Cryptography/Hashes/hash_short.txt", "r")
    
    salts = []
    prints = []

    for hash in hash_f:
        stripped = hash.strip('\n')
        salt, f_print = process_hashes(stripped)
        salts.append(salt)
        prints.append(f_print)

    print(salts)
    print(prints)

#Output:
['533', '558', '422', '925', '870', '509', '553', '956', '974', '747']

['2e14e930ae23430c3613b5a34d9869ec', 'cc0620d9c916c22a4df0ee8053859176', 
'4ce2cafc792736891c64cf1ff3c51dd7', 'bc10172c01f2b14a200788f3ea29ebdd', 
'6e4a563bd486d070892c4bbd1748d9e4', 'c26febe17848c0d630c2e66b0dda3b5f', 
'0075d7f92bad4ca656155c8de348c723', '17343db5b89d8044d478b5c4e8421ba2', 
'1f07e4f4929e88dfccea1111cd1eb804', 'a1ff0ee5deda0cd4122fa889cdb6e4f8']


#BLUEPRINT-------------------------------------------------------
# input to be hashed
# mystring = input('Enter string to hash: ') 
# salt = str(random.randint(409, 1009))
# #input + salt
# salted = mystring + salt

# hash_obj = hashlib.md5(salted.encode())

# finger_print = hash_obj.hexdigest() 
# print(f'hash/finger_print: {finger_print}')
# ------------------------------------------------------------------
''' now you need a small script to take everything on the hash_short.txt and salt it, store the salt in a list,
store the hashes in a list
-move the hashed to salted_hash.txt
-run salted_hash.txt through the hashvalidator.py'''




# what do I do with the salt and fingp to store them
# s, fp = process_hashes(hash)
# salts.append(s)
# finger_prints.append(fp)