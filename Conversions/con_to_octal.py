#!/usr/bin/python3

# Converts a Decimal e.g. 39, to an octal while showing the process of conversion

number = ""

while(not(number.isnumeric())):
    
    number = input("What is the decimal to convert? ")
    temp_numb = int(number)
    bin_output = ""
     
    while(temp_numb > 0):
    
        print(f"{temp_numb} / 8 = ", int(temp_numb / 8), "R", temp_numb % 8)    
        bin_output = str(temp_numb % 8) + bin_output
        temp_numb = int(temp_numb / 8)

    print(f"{number} in octal:", bin_output)     