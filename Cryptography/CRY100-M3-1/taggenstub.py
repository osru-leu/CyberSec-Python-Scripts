#!/usr/bin/python3

import hmac
import sys

def gen_tag(msg, key):
    hm = hmac.new(key.encode(), digestmod="md5")
    hm.update(msg.encode())
    return hm.hexdigest()

if __name__ == '__main__':
    # keyfilename = 'master.key'
    # datafilename = 'tags.txt'
    keyfilename = 'c:/users/ursos/desktop/school/thonnyprogs/cryptography/cry100-m3-1/master.key'
    datafilename = 'c:/users/ursos/desktop/school/thonnyprogs/cryptography/cry100-m3-1/tags.txt'

    with open(keyfilename) as f:
        key = f.read()

    with open(datafilename) as g:
        data = g.read()

    '''1. How do I do the below sequence for each line in tags.txt??????
            split data isnt working in total for your purpose.************
       2. then compare calculated hmac to the existing hmac in tags.txt
       split_data is both sentence and hmac
        split_data[0] -> sentence
        split_data[1] -> hmac and the next sentence
            -maybe split again?
            
            .split() splits a string into a list'''    
    for string in data:
        # note: data[0:2] == My
        # print(data[0:2])
        if ":" in string:
            split_data = data.split(":", 1) #START HERE THIS MAKES A LIST OF 2 ITEMS
        # split_data = data.split(":")
            print(f'split data :{split_data}------------------------------------------------------------------------------\n')
    # print(f'split data 0: {split_data[0]}')
    # h_mac = split_data[1].strip('\n')
    # print(f'hmac of sentence: {h_mac}-----------------\n')
    # print(f'split data 1: {split_data[1]}')
        # mess = gen_tag(split_data[0], key)
        # # print(split_data[1]) # This is printing the second line of tags.txt
        # if mess == split_data[1]:
        #     print(f'Data True: {split_data[1]}')
        
        
        # if "." in data[:]:
            # print(data.split("."))
            # split_data = data.split(":")
            # mess = gen_tag(split_data[0], key)
    # print(mess)
          
        
    f.close()
    g.close()

    '''ONe option:
        for sentence in split_data:
            take every other index (string) and send it through gen_tag()'''