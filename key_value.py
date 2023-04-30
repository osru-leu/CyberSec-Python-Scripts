#!/usr/bin/python3
letters = {}
 
user_word = input("What word or phrase do you want to analyze? ").upper()
 
for lett in user_word:
    if lett in letters.keys():
        letters[lett] += 1
        print('letters -> ', letters)
    else:
        letters[lett]=1
        print('else')
         
for key, value in letters.items():
    print(key + " occurs " + str(value) + " times")