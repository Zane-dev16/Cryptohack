from .legendre import legendre

## Following Tonneli Shanks Alg from https://en.wikipedia.org/wiki/Tonelli%E2%80%93Shanks_algorithm
def factorize_2s(num):
    Q = num
    S = 0
    while (True):
        if (Q % 2):
            return Q, S
        Q //= 2
        S += 1

def find_z(p):
    for z in range(1, 100):
        if (legendre(z, p) == -1):
            return z

def find_i(t, M, p):
    for i in range(1, M):
        t = pow(t, 2, p)
        if (t == 1):
            return i
    raise ValueError("i not found")

def find_r(M, c, t, R, p):
    while (True):
        if (t == 0):
            return 0
        if (t == 1):
            return R
            break

        i = find_i(t, M, p)
        b = pow(c, 2 ** (M - i - 1), p)
        M = i
        c = pow(b, 2, p)
        t = (t * c) % p
        R = (R * b) % p

def tonelli_shanks(n, p):
    if (legendre(n, p) != 1):
        raise ValueError("a is not a quadratic residue")

    Q, S = factorize_2s(p-1) 
    z = find_z(p)

    M = S
    c = pow(z, Q, p)
    t = pow(n, Q, p)
    R = pow(n, (Q+1)//2, p)
    return find_r(M, c, t, R, p)
