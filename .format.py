#Formating Lab


print("The letter '{}' is {} in Ascii".format('A', ord('A')))
letter = 'Q'
print("The letter {this} is {that} in binary".format(this=letter, that=ord(letter)))
print("The letter {that} is {this} in binary".format(this=letter, that=ord(letter)))
print("The letter {1} is {0} in binary".format(ord('X'), 'X')) #using indexing [0,1,2]
#let = input("Please type a letter: ")
#print("The letter {} is {} in Ascii".format(let, ord(let)))
print("The letter '{:15}' is taking 15 characters".format('something')) #telling the format
# bracket to take up to 15 spaces
print("The letter '{:>15}' is taking 15 characters".format('something')) # moving the characters to the
# front of the 15 characters

print("The letter '{:<15}' is taking 15 characters".format('something'))
print("The letter '{:^15}' is taking 15 characters".format('something')) # centering the string
# in the 15 spaces
print('--------------------------------------------------')

myDict = {'Crypto': 3, 'Sys': 5, 'Net': 5,
          'GRC': 2, 'Threat': 2, 'Python': 2,
          'Logs': 3, 'AppSec': 2, 'Capstone': 1}

print("{:^15}\t{:^7}".format("Course", "Modules"))
print("{:^15}\t{:^7}".format("-"*15, "-"*7))

for course in myDict.keys():
    print("{:^15}\t{:^7}".format(course, myDict[course]))

