def gcd(num1, num2):
    if (num2 > num1):
        return gcd(num2, num1)
    
    rest = num1 % num2
    if (rest == 0):
        return num2
    else:
        return gcd(num2, rest)

a, b = 66528, 52920
print(gcd(a, b))