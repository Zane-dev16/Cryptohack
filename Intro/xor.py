from pwn import xor

label = "label"
integer = 13

unicode_list = [ord(char) for char in label]
xorred_list = [unicode ^ 13 for unicode in unicode_list]
ret_char_list = [chr(o) for o in xorred_list]

print(xor(label, integer))