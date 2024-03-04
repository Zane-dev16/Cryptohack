from pwn import xor

cipher = int("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf", 16)
key1 = int("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313", 16)
semi_decrypted = cipher ^ key1
key2 = int("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1", 16)
flag = semi_decrypted ^ key2

cipher = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")
key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
key2 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")

def xor_bytes(bytes1, bytes2):
    # Convert bytes to integers
    result_bytes = [byte1 ^ byte2 for byte1, byte2 in zip(bytes1, bytes2)]

    return bytes(result_bytes)

print(xor_bytes(xor_bytes(cipher, key1), key2))