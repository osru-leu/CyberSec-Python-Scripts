n = 10
s = ""
while n > 0:
    s = str(n % 5) + s
    n /= 5
print(s)

