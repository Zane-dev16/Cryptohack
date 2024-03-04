from pwn import xor
input_str = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

key = bytes([input_byte ^ ord(char) for input_byte, char in zip(input_str, "crypto{")])
key += bytes([input_str[-1] ^ ord("}")])

print(key)

print(xor(key, input_str))
