
# The first for loop below ouputs A-Z and a-z with their corresponding ascii number
# The second loop only outputs a-z (lowercase) with their corresponding ascii number

for num, let in zip(range(65, 91), range(97, 123)):
    print(num, chr(num), let, chr(let))
    
for let in range(97, 123):
    print(let, chr(let))
print(num, chr(num), let, chr(let))
