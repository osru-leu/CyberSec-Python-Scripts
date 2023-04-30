myDict = {}
myDict["fruit"] = "Apple"
print(myDict["fruit"])
print(myDict)

print("Fruit" in myDict.keys())
print("fruit" in myDict.values())
myDict['Cat'] = 'Not Fruit'
print(myDict.values())
for x in myDict:
    print(x)
print(myDict.clear())

test_dict = {"a":print('a key')}
print(test_dict)
print(test_dict["a"])