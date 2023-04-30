#print(28 % 26)
values = "0123456789abcdefghijklmnopqrstuvwxyz"
# usr_in = input("input a char from values ")
# for char in usr_in:
#     print(char)
#     if usr_in[char] == values[char]:
#         print(char)
#------------------------------------------------test work through-------
number = input("Type decimal: ")
# base = int(input())
for char in number:
    #char[0]
    print(number.find(char))

    if char in values[10:]:# do this later
        print(f'letter character: {char}')
''''number[] * (base**position[-1])
for each digit in number'''
#char * base**number[]
print(f'last character of number: {char[-1]}')



'''Do I need to loop through both usr_in and values?
    No bc indices can be used
    
    What am I trying to do?
        -You are taking the result of finding applying a base number (the number given as a result of finding a base, e.g.
        hex(), oct(), bin() or any other random base chosen.
        -You are converting the res_of_base back to a decimal by multiplying
        each digit in its numeric position by the base to the inth power of its position.
        Then, find the sum which your decimal
        Example:
        hex()
        -'''


#curr