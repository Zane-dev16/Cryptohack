def legendre(n, p):
    legendre = pow(n, (p-1)//2, p)
    if (legendre != 1):
        legendre -= p
    return legendre