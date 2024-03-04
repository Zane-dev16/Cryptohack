
from pwn import xor

bytes = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
print(xor(bytes, b'\x10'))

key = bytes[0] ^ ord("c")

for byte in bytes:
    print()