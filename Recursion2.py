# 2^4=16
def power(num, pwr):
    if pwr == 0:
        return 1
    else:
        return num * power(num, pwr-1)
 

# e.g.: 5!=5x4x3x2x1
# 0!=1
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

print("{} to the power of {} is {}".format(5, 3, power(5, 3)))
print("{}! is {}".format(4, factorial(4)))
