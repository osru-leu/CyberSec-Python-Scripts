#!/usr/bin/python3
#Author: Sam Urso
#Date: 6.6.2022
#version: 1.0

'''
Open .txt file
Output any lines without the string "line" in them
from txt file
'''

filename = "example.txt"
fh = open(filename)

for line in fh:
    if "line" not in line:
        print(line)

fh.close

# Output even lines only:

#num = 1
# for line in fh:
#     if num % 2 == 0:
#         print(line)
#     num += 1
# fh.close