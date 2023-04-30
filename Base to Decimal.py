#!usr/bin/python3
'''The goal of the following code is:
MAIN OVERALL GOAL:
    **Find the binary value of a number given by the user**
You will need to:
    1. Get user input
        -ask for a number to convert to binary 
    2. Find the remainder of the number given of the base 2 (user_num % 2)
    3. Find the quotient of the user number using base 2 (user_num / 2)
    4. Store the remainder
    5. Store the quotient
    6. perform step 2 and step 3 on the new quotient
    7. store the new quotient
    8. store the new remainder
    9. continue steps 2 through 6 until the quotient is 0
    10. output the remainder
'''

# number = ""
# while (not(number.isnumeric())):
#     number = input("What is the decimal to convert ? ")
#     temp_numb = int(number)
#     remainder = ""
    
#     while (temp_numb > 0):
#         print_remain = temp_numb % 2 
#         remainder = str(temp_numb % 2) + remainder
#         temp_numb = int(temp_numb / 2) #
#         print(f'{number} / 2 = {print_remain}')
#     print(remainder)


'''The goal of the following code is:
MAIN OVERALL GOAL:
    **Find the value of a number given by the user by the base number they provide**
You will need to:
    1. Get user input
        -ask for a number to convert to binary 
        -ask for a base number by which to convert 
    2. Find the remainder of the number given of the base given (user_num % base)
    3. Find the quotient of the user number using base given (user_num / base)
    4. Store the remainder
    5. Store the quotient
    6. perform step 2 and step 3 on the new quotient
    7. store the new quotient
    8. store the new remainder
    9. continue steps 2 through 6 until the quotient is 0
    10. output the remainder
'''
# print(hex(1000))
# print(bin(126))


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

'''
1. take the number as a string -input()
2. Split it into its individual pieces - 
    for num in numbers:
        perform the equation on num
3. convert the individual pieces into integers
4. for the length of the string multiply each individual piece by the base...
    the base is raised to the power of the individual numbers position in reverse so for example:
    192
    (1 * 10**2) + (9 * 10**1) + (2 * 10**0)  
    
    
for letter values check the index of the letter in values and implant the index value into the equation.
make non letters work first.     
    
'''
# print(bin(42))          
         
'''So, hex 192 is 
(1 * 16**2) + (9 * 16**1) + (2 * 16**0) 

= 256 + 144 + 2 

= 402'''
# decimal = 0
# base = 16  
# nums = "192"
# for num in nums:
#     # print(f'num {num}')
#     # print(f'Index -1 value-> {nums[-1]}')
#     numb = int(num)
#     # print(f'numb int -> {numb}')
#     print(f'{numb} * {base} ** {int(nums[-2])}')
#     decimal = (numb * base**int(nums[-2])) + (numb * base**int(nums[-1])) + (numb * base**int(nums[0]))
    
# print(decimal)
   
base = 16  
nums = "192"
numsLen = len(nums)
print(range(-1, numsLen))
# for num in nums:
#     number = int(num)
#     # print(number)
#     for index in range(len(nums[:])):
#         print(f'index -> {index}')
#         # print(f'Index -1 value-> {nums[-1]}')
#         numb = int(index)
#         # print(f'numb int -> {numb}')
#         # decimal = (numb * base**int(nums[1])) + (numb * base**int(nums[-1])) + (numb * base**int(nums[0]))
#         print(f'{number} * {base} ** {index}')
#         # print(decimal)


for i in range(-1, numsLen):
    print(i)