#!/usr/bin/python3

# Converts a decimal e.g. 97, to its binary value. Shortend version of decimal_to_binary.py
# which has a line by line explanation of what the code is doing. This was an early assignment in Flatiron School   

#mynumber = 97
output = ""
myvalue = 97
while (myvalue > 0):
    myremainder = myvalue % 2
    print(f'my remainder {myremainder}')
    output = str(myremainder) + output
    myvalue = int(myvalue/2)
    print('myvalue = ', myvalue)
print(output)    
