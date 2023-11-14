myvar1 = 5
myvar2 = 0
#print(myvar1 / myvar2)
mycount = 0
outputeven=0
outputodd=0

for mycount in range(0,15):
    print(f'mycount {mycount}')
    if (mycount /2 == int(mycount/2)):
        outputeven += mycount
        print(f'outputeven {outputeven}')
    else:
        outputodd += mycount
        print(outputodd)
print("Even:", outputeven, " Odd:", outputodd)

file = open("example.txt")