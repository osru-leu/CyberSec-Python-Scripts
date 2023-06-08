



# number = ""
# values = "0123456789abcdefghijklmnopqrstuvwxyz"

# while (not(number.isnumeric())):
#     number = input("What is the decimal to convert ? ")
#     base = int(input("By which base would you like to convert? "))
#     temp_numb = int(number)
#     remainder = ""
    
#     while (temp_numb > 0):
        
#         int_remainder = temp_numb % base 
       
#         if int_remainder >= 10:
#             rem_index = values[int_remainder]
#             remainder = str(rem_index) + remainder
            
#         else:
#              remainder = str(temp_numb % base) + remainder 
#         temp_numb = int(temp_numb / base)

#         print(f'{number} / {base} = {int_remainder}')
#     print(remainder)

# number = input("What is the number you would like to convert to decimal? ")
# base = int(input("By which base would you like to convert? "))

# solution = int(number, base)

# print(solution)

#---------------------------------------------------------------------------------------------------------------

print(oct(126))
print(hex(126))
print(bin(1001))

values = "0123456789abcdefghijklmnopqrstuvwxyz"
number = input("What is the number you would like to convert to decimal? ")
base = int(input("By which base would you like to convert? "))

digits = []
result = 0

for i in number:
    # print(i, 'i********')
    if i >= values[10]:
        digits.append(values.index(i))
    else:
        digits.append(int(i))
digits = digits[::-1]# look this up how does it reverse the string?
print(f'digits reversed: {digits}')

for num in range(len(digits)):
    print('Number', num)
    print(f'{result} + {digits[num]} * {base}**{num}')
    result += digits[num]*base**num
    print('result', result)
print(result)

