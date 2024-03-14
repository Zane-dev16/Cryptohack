
def mod_inv(num, m):
    num1, num2 = m, num
    xi_prev = 0
    xi = 1
    while (True):
        rest = num1 % num2
        quocient = num1 // num2
        if (rest == 0):
            if (num2 != 1):
                raise ValueError("numbers are not coprime")
            return xi

        else:
            xi_new = xi_prev - (xi * quocient)
            xi_prev = xi
            xi = xi_new

            num1 = num2
            num2 = rest

def prod(nums):
    p = 1
    for num in nums:
        p *= num
    return p

def crt(a_list, n_list):
    M = prod(n_list)
    result = 0
    for i in range(len(a_list)):
        Mi = M / n_list[i]
        Mi_inv = mod_inv(Mi, n_list[i])
        result += Mi * Mi_inv * a_list[i]

    while (result < 0):
        result += M
    return int(result)

x = crt((2, 3, 5), (5, 11, 17))
print(x)
