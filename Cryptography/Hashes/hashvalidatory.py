import hashlib


if __name__ == "__main__":
    letters = "abcdefghijklmnopqrstuvwxyz"
    filename = "C:/Users/ursos/Desktop/School/Scripts/Cryptography/Hashes/hash_short.txt"
    
    try:
        f=open(filename)
        print(f)
        inputtext = f.read()
        print(f'input text:\n{inputtext}')
    except:
        f="error"
        print(f)

    # hashes=[] # 
    
    hashes = inputtext.split("\n")

    for let1 in letters:
        for let2 in letters:
            for let3 in letters:
                for let4 in letters:
                    for let5 in letters:
                        testvalue = let1 + let2 + let3 + let4 + let5
                        hash_obj = hashlib.md5(testvalue.encode())
                        if hash_obj.hexdigest() in hashes:
                            print(testvalue, hash_obj.hexdigest())