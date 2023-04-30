#!/usr/bin/python3


decimal = ""

values = "0123456789abcdefghijklmnopqrstuvwxyz"

while(not(decimal.isnumeric())):
    # take input from the user:
    decimal = input("What is the decimal to convert? ")
    base = int(input("What base would you like to convert? "))
    # set user string input to an integer variable:
    number = int(decimal)
    output = ""
     
    while(number > 0):
        # show process:
        print(f"{number} / {base} = ", int(number / base), "R", number % base)
        # find the remainder of variables decimal and base:
        remainder = number % base
        
        if remainder >= 10:
            # set remainder to the indice value of the string "values" if the remainder is greater than or equal to 10: 
            remainder = values[remainder]
            # add the remainder to the output string:
            output = str(remainder) + output
        # if the remainder is not greater than 10, convert it to a string, add to output:  
        else:
            output = str(remainder) + output
        # decrement "number" to break while loop    
        number = int(number / base)
        
    print(f"{decimal} of base {base}:", output)
    
    

