def largestInt(a, b):
    if a < b:
        return b
    else:
        return a



if __name__ == "__main__":

    int1 = 3
    int2 = 5

    print("{} is the larger of {} and {}".format(largestInt(int1, int2,), int1, int2))