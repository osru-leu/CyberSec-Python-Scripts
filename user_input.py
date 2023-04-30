classList = []

userClass = ""

while (userClass != "DONE"):
    userClass = input("What classes do you like (Type 'DONE' when done)?").upper()
    if (userClass == "DONE"):
        break
    else:
        classList.append(userClass)
        
        
print("You like the following classes: ")

for cl in classList:
    print(cl)