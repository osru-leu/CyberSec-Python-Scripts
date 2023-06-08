#!/usr/bin/python3

number = ""

while(not(number.isnumeric())):
    
    base = input("What base would you like to convert to (OCT, HEX, or BIN)? ").upper()  
    number = input("What is the decimal to convert? ")
    
    temp_numb = int(number)
    
    bin_output = ""
     
    while(temp_numb > 0):
        
        if base == "OCT":
            
            print(f"{temp_numb} / 8 = ", int(temp_numb / 8), "R", temp_numb % 8)
            
            bin_output = str(temp_numb % 8) + bin_output
             
            temp_numb = int(temp_numb / 8)
            
        elif base == "BIN":
            
            print(f"{temp_numb} / 2 = ", int(temp_numb / 2), "R", temp_numb % 2)
            
            bin_output = str(temp_numb % 2) + bin_output
             
            temp_numb = int(temp_numb / 2)
            
        elif base == "HEX":
            print(f"{temp_numb} / 16 = ", int(temp_numb / 16), "R", temp_numb % 16)
            
            bin_output = str(temp_numb % 16) + bin_output
             
            temp_numb = int(temp_numb / 16)
            
                
        
    print(f"{number} in {base}:", bin_output)
    
    
# 1. Set variable to an empty string for later storage
# 2. while the variable "number" is not numeric, execute. not() is used because the variable "number" is a string.
# 3. Take user input- input() function stores objects as a string
# 4. Set string variable "number" to a new variable "temp_numb" as an integer
# 5. Set a variable to an empty string for later storage and result output.
# 6. while var "temp_numb" is greater than 0, execute. When "temp_numb" is less than 0, stop.
# 7. Print statement ouputing the execution process of the code below
# 8. Find the remainder of temp_numb, convert remainder to a string, add remainder to variable bin_output,
#    and store the result in bin_output.
# 9. Divide temp_numb by 8, store the result as an integer in variable temp_numb.
# 10. Code execution returns to line 15 with the new result stored in temp_numb. If temp_numb is greater than 0,
#    execution continues. 
# 11. Print the result "bin_ouput" when "temp_numb" is less than 0.
