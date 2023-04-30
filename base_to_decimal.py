#!/usr/bin/python
# 5/4/2022
# Sam Urso


print(oct(126))
print(hex(126))
print(bin(1001))

values = "0123456789abcdefghijklmnopqrstuvwxyz"
number = input("What is the number you would like to convert to decimal? ")
base = int(input("By which base would you like to make this conversion? "))

digits = []
decimal = 0

for i in number:
    if i >= values[10]:
        digits.append(values.index(i))
    else:
        digits.append(int(i))
digits = digits[::-1]

for num in range(len(digits)):
    #print(f'{decimal} + {digits[num]} * {base}**{num}')
    decimal += digits[num]*base**num

print(decimal)


'''
Line 3. A funciton to test against
Line 4. A funciton to test against
Line 5. A funciton to test against

Line 7. values string variable
Line 8. number var taking in a string
Line 9. base var taking an integer

Line 11. Empty list for appending
Line 12. var set to 0 for later integer storage and output

Line 14. for each string(individual character) in the var 'number'..
Line 15. if the character's value is greater than or equal to the index 10 of values..
Line 16. ...append the index value of the string to empty list digits
Line 17. else(if) the string is not in an index position greater than or equal to 10...
Line 18. ...append the string as an integer to the list digits.
Line 19. reverse the order of the contents of the list digits.

Line 22. for each index position ('num') for the length of list digits e.g. 0, 1, 2, etc.

Line 23. multiply the number in the 'num' position of the list digits, by the var 'base'
         raised to the power of num(the current index position of digits), plus
         the var 'result'. Once the equation is calculated, the value is set to the variable
         'result'.
         
         



'''