def largestInt(a, b):
    if a < b:
        return b
    else:
        return a




int1 = 3
int2 = 5

print("Inside myfuncdundername.py, __name__ var currently contains " + __name__)
print("{} is the larger of {} and {}".format(largestInt(int1, int2,), int1, int2))