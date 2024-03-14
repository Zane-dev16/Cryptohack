from random import randint

a = 288260533169915
p = 1007621497415251

FLAG = b'crypto{????????????????????}'


def encrypt_flag(flag):
    ciphertext = []
    plaintext = ''.join([bin(i)[2:].zfill(8) for i in flag])
    for b in plaintext:
        e = randint(1, p)
        n = pow(a, e, p)
        print((pow(-n,(p-1)//2,p)))
        if b == '1':
            ciphertext.append(n)
        else:
            n = -n % p
            ciphertext.append(n)
    return ciphertext

super_list = [bin(i)[2:] for i in FLAG]
print([chr(int(binary, 2)) for binary in super_list])
print(encrypt_flag(FLAG))
