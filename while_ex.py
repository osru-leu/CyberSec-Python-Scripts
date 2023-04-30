#!/usr/bin/python3
''' my value 97, in binary '''
#mynumber = 97
output = ""
myValue = 97
while (myValue > 0):
    myRemainder = myvalue % 2
    print(f'my remainder {myRemainder}')
    output = str(myRemainder) + output
    myValue = int(myValue/2)
    print('myValue = ', myValue)
print(output)    
