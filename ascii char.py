#!/usr/bin/python3

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
