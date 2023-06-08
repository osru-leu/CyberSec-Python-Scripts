#!/usr/bin/python3

# set variable to an empty string for later storage
number = ""

# while the variable "number" is not numeric, execute. not() is used because the variable "number" is a string.
while(not(number.isnumeric())):
    # Take user input- input() function stores objects as a string  
    number = input("What is the decimal to convert? ")
    # Set string variable "number" to a new variable "temp_numb" as an integer
    temp_numb = int(number)
    # Set a variable to an empty string for later storage and result output.
    bin_output = ""
    # while var "temp_numb" is greater than 0, execute. When "temp_numb" is less than 0, stop. 
    while(temp_numb > 0):
        # Print statement ouputing the execution process of the code below
        print(f"{temp_numb} / 2 = ", int(temp_numb / 2), "R", temp_numb % 2)
        # Find the remainder of temp_numb, convert remainder to a string, add remainder to variable bin_output,
        # and store the result in bin_output.
        bin_output = str(temp_numb % 2) + bin_output
        # Divide temp_numb by 2, store the result as an integer in variable temp_numb. 
        temp_numb = int(temp_numb / 2)
        # Code execution returns to line 15 with the new result stored in temp_numb. If temp_numb is greater than 0,
        # execution continues. 
    # Print the result "bin_ouput" when "temp_numb" is less than 0. 
    print(f"{number} in binary:", bin_output)

# check the program against the built-in binary function bin()
print(bin(int(number)))
