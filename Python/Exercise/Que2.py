def sumnum(num):
    previousnum = 0
    for i in range(num):
        sum = previousnum + i
        print("Current Number", i, "Previous Number ", previousnum, "Sum: ", sum)
        previousnum = i

print("Printing current and previous number sum in a given range(number)")
sumnum(int(input()))