def get_bezout_coefs(num1, num2):
    if (num2 > num1):
        temp = num2
        num2 = num1
        num1 = temp

    xi_prev, yi_prev = 1, 0
    xi, yi = 0, 1
    while (True):
        rest = num1 % num2
        quocient = num1 // num2
        if (rest == 0):
            return xi, yi

        else:
            xi_new = xi_prev - (xi * quocient)
            yi_new = yi_prev - (yi * quocient)
            xi_prev, yi_prev = xi, yi
            xi, yi = xi_new, yi_new

            num1 = num2
            num2 = rest

a, b = 26513, 32321
print(get_bezout_coefs(a, b))